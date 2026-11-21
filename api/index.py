import os
import json
import subprocess
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# The root directory for the files is one level up from the 'api' folder
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def get_file_tree(dir_path):
    tree = []
    for entry in os.scandir(dir_path):
        if entry.name.startswith('.') or entry.name in ['api', 'node_modules', 'css', 'js', '__pycache__']:
            continue
        if entry.is_dir():
            children = get_file_tree(entry.path)
            if children:
                tree.append({
                    "name": entry.name,
                    "type": "directory",
                    "path": os.path.relpath(entry.path, BASE_DIR).replace('\\', '/'),
                    "children": children
                })
        elif entry.name.endswith('.py') or entry.name.endswith('.ipynb'):
            tree.append({
                "name": entry.name,
                "type": "file",
                "path": os.path.relpath(entry.path, BASE_DIR).replace('\\', '/')
            })
    return sorted(tree, key=lambda x: (x['type'] == 'file', x['name']))

@app.route('/api/files', methods=['GET'])
def list_files():
    tree = get_file_tree(BASE_DIR)
    return jsonify(tree)

@app.route('/api/file', methods=['GET'])
def get_file():
    file_path = request.args.get('path')
    if not file_path:
        return jsonify({"error": "Path required"}), 400
    
    full_path = os.path.join(BASE_DIR, file_path.replace('/', os.sep))
    if not os.path.exists(full_path) or not full_path.startswith(BASE_DIR):
        return jsonify({"error": "File not found"}), 404
    
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            if full_path.endswith('.ipynb'):
                # Parse notebook
                notebook = json.load(f)
                code_cells = []
                for cell in notebook.get('cells', []):
                    if cell.get('cell_type') == 'code':
                        source = "".join(cell.get('source', []))
                        if source.strip():
                            code_cells.append(source)
                content = "\n\n# --- Next Cell ---\n\n".join(code_cells)
                return jsonify({"content": content, "type": "python"})
            else:
                return jsonify({"content": f.read(), "type": "python"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/execute', methods=['POST'])
def execute_code():
    data = request.json
    code = data.get('code')
    stdin_data = data.get('stdin', '')
    
    if not code:
        return jsonify({"error": "No code provided"}), 400
    
    # Write to a temp file
    temp_path = os.path.join(BASE_DIR, 'temp_exec.py')
    try:
        with open(temp_path, 'w', encoding='utf-8') as f:
            f.write(code)
            
        result = subprocess.run(
            ['python', temp_path],
            capture_output=True,
            text=True,
            input=stdin_data,
            timeout=5
        )
        output = result.stdout
        if result.stderr:
            output += "\n[Error]\n" + result.stderr
        return jsonify({"output": output})
    except subprocess.TimeoutExpired:
        return jsonify({"output": "[Error] Execution timed out (max 5 seconds)."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

# Serve static files for production/Vercel
@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/<path:path>')
def static_files(path):
    if os.path.exists(os.path.join(BASE_DIR, path)):
        return send_from_directory(BASE_DIR, path)
    return send_from_directory(BASE_DIR, 'index.html')

# Vercel requires app as the WSGI handler
if __name__ == '__main__':
    app.run(port=5002, debug=True)
