let currentFilePath = '';

document.addEventListener('DOMContentLoaded', () => {
    loadFiles();

    // Editor sync with line numbers
    const editor = document.getElementById('code-editor');
    const lineNumbers = document.getElementById('line-numbers');

    editor.addEventListener('input', () => {
        const lines = editor.value.split('\n').length;
        lineNumbers.innerHTML = Array(lines).fill(0).map((_, i) => i + 1).join('<br>');
    });
    
    editor.addEventListener('scroll', () => {
        lineNumbers.scrollTop = editor.scrollTop;
    });
    
    // Tab support
    editor.addEventListener('keydown', function(e) {
        if (e.key === 'Tab') {
            e.preventDefault();
            const start = this.selectionStart;
            const end = this.selectionEnd;
            this.value = this.value.substring(0, start) + "    " + this.value.substring(end);
            this.selectionStart = this.selectionEnd = start + 4;
        }
    });
});

async function loadFiles() {
    const treeContainer = document.getElementById('file-tree');
    treeContainer.innerHTML = '<div class="text-center p-4 text-slate-500 text-sm"><i class="ph ph-spinner animate-spin"></i> Loading...</div>';
    
    try {
        // When hosted on Vercel or locally, the API is relative
        const res = await fetch('/api/files');
        const tree = await res.json();
        treeContainer.innerHTML = renderTree(tree);
    } catch (err) {
        treeContainer.innerHTML = `<div class="text-rose-400 p-4 text-xs">Failed to load files: ${err.message}</div>`;
    }
}

function renderTree(nodes) {
    let html = '';
    for (const node of nodes) {
        if (node.type === 'directory') {
            html += `
                <div>
                    <div class="folder-item">
                        <i class="ph-fill ph-folder text-blue-400"></i> ${node.name}
                    </div>
                    <div class="indent">
                        ${renderTree(node.children)}
                    </div>
                </div>
            `;
        } else {
            const isIpynb = node.name.endsWith('.ipynb');
            const icon = isIpynb ? '<i class="ph-fill ph-notebook text-orange-400"></i>' : '<i class="ph-fill ph-file-py text-yellow-400"></i>';
            html += `
                <div class="file-item" onclick="openFile('${node.path}', this)">
                    ${icon} <span class="truncate">${node.name}</span>
                </div>
            `;
        }
    }
    return html;
}

async function openFile(path, element) {
    // Update active state in sidebar
    document.querySelectorAll('.file-item').forEach(el => el.classList.remove('active'));
    if (element) element.classList.add('active');

    document.getElementById('current-file-name').innerHTML = `<i class="ph ph-spinner animate-spin text-yellow-500"></i> Loading ${path}...`;
    
    try {
        const res = await fetch(`/api/file?path=${encodeURIComponent(path)}`);
        const data = await res.json();
        
        if (data.error) {
            alert('Error loading file: ' + data.error);
            document.getElementById('current-file-name').innerHTML = `<i class="ph ph-warning text-rose-500"></i> Error`;
            return;
        }

        const editor = document.getElementById('code-editor');
        editor.value = data.content;
        currentFilePath = path;
        
        // Update filename header
        const isIpynb = path.endsWith('.ipynb');
        const icon = isIpynb ? '<i class="ph-fill ph-notebook text-orange-400"></i>' : '<i class="ph-fill ph-file-py text-yellow-400"></i>';
        document.getElementById('current-file-name').innerHTML = `${icon} ${path.split('/').pop()}`;
        
        // Trigger input event to update line numbers
        editor.dispatchEvent(new Event('input'));
        
        appendToTerminal(`\n> Loaded ${path} (Parsed: ${data.type})`);
    } catch (err) {
        alert('Failed to fetch file: ' + err.message);
    }
}

async function runCode() {
    const code = document.getElementById('code-editor').value;
    const rawStdin = document.getElementById('stdin-input').value;
    const stdin = rawStdin.replace(/\\n/g, '\n'); // Allow user to type \n for multiple inputs
    
    if (!code.trim()) {
        appendToTerminal('\n[Error] No code to run.');
        return;
    }

    appendToTerminal(`\n> Executing code...`);
    
    try {
        const res = await fetch('/api/execute', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ code, stdin })
        });
        const data = await res.json();
        
        if (data.error) {
            appendToTerminal(`\n[Execution Error]\n${data.error}`);
        } else {
            appendToTerminal(`\n[Output]\n${data.output || '(No output)'}`);
        }
    } catch (err) {
        appendToTerminal(`\n[Server Error] Failed to reach /api/execute.\nMake sure the Flask backend is running!`);
    }
}

function appendToTerminal(text) {
    const term = document.getElementById('terminal-output');
    term.innerHTML += text + '\n';
    term.parentElement.scrollTop = term.parentElement.scrollHeight;
}

function clearTerminal() {
    document.getElementById('terminal-output').innerHTML = '<span class="text-slate-500">Terminal cleared.</span>\n';
}
