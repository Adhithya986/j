/**
 * Eclipse IDE Interface Engine
 * Authentic look, tabs, syntax highlighter, tree explorer, search, and one-click copy
 */

(function () {
  'use strict';

  // State
  let allPrograms = [];
  let openTabs = [];
  let activeProgramId = null;
  let activeBottomTab = 'console';
  let breakpoints = new Set(); // store "progId:lineNum"

  // Eclipse Icons SVG Library
  const ICONS = {
    eclipse: `<svg viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="15" fill="#2C2255"/><path d="M4 12h24M2 16h28M4 20h24" stroke="#F58025" stroke-width="2.5" stroke-linecap="round"/><circle cx="16" cy="16" r="8" fill="#FDB813"/></svg>`,
    project: `<svg viewBox="0 0 16 16"><path fill="#fbc02d" d="M1 3h5l2 2h7v9H1z"/><path fill="#1565c0" d="M11 6v5l3-2.5z"/></svg>`,
    srcFolder: `<svg viewBox="0 0 16 16"><path fill="#78909c" d="M1 3h5l1.5 1.5H15v9H1z"/><path fill="#4caf50" d="M7 6h6v5H7z"/></svg>`,
    package: `<svg viewBox="0 0 16 16"><path fill="#bcaaa4" d="M2 4l6-3 6 3v8l-6 3-6-3z"/><path fill="#8d6e63" d="M2 4l6 3 6-3M8 7v8"/></svg>`,
    javaClass: `<svg viewBox="0 0 16 16"><circle cx="8" cy="8" r="7" fill="#4caf50"/><text x="8" y="11" text-anchor="middle" font-size="10" font-weight="bold" fill="#fff" font-family="sans-serif">C</text></svg>`,
    javaInterface: `<svg viewBox="0 0 16 16"><circle cx="8" cy="8" r="7" fill="#1e88e5"/><text x="8" y="11" text-anchor="middle" font-size="10" font-weight="bold" fill="#fff" font-family="sans-serif">I</text></svg>`,
    library: `<svg viewBox="0 0 16 16"><path fill="#7e57c2" d="M3 2h10v12H3z"/><path fill="#b39ddb" d="M5 2h2v12H5zm4 0h2v12H9z"/></svg>`,
    jar: `<svg viewBox="0 0 16 16"><path fill="#ffb74d" d="M4 2h8v2H4zm-1 3h10v9H3z"/><circle cx="8" cy="9" r="2.5" fill="#f57c00"/></svg>`,
    method: `<svg viewBox="0 0 16 16"><circle cx="8" cy="8" r="5" fill="#ffb300"/><text x="8" y="10" text-anchor="middle" font-size="7" font-weight="bold" fill="#fff">m</text></svg>`,
    field: `<svg viewBox="0 0 16 16"><rect x="3" y="3" width="10" height="10" rx="2" fill="#42a5f5"/></svg>`,
    run: `<svg viewBox="0 0 16 16"><circle cx="8" cy="8" r="7" fill="#43a047"/><path fill="#fff" d="M6.5 4.5v7l5-3.5z"/></svg>`,
    debug: `<svg viewBox="0 0 16 16"><path fill="#e53935" d="M8 2a3 3 0 00-3 3v1h6V5a3 3 0 00-3-3zm-4 5h8v4a4 4 0 01-8 0V7zm-2 1h2m8 0h2m-11 3h2m8 0h2m-10-6l2 1.5m6-1.5l-2 1.5" stroke="#e53935" stroke-width="1.5"/></svg>`,
    copy: `<svg viewBox="0 0 16 16"><path fill="currentColor" d="M4 2h7a1 1 0 011 1v1H4V2z"/><rect x="4" y="4" width="9" height="10" rx="1" fill="currentColor" fill-opacity="0.3"/><rect x="2" y="2" width="9" height="10" rx="1" stroke="currentColor" stroke-width="1.5" fill="none"/></svg>`,
    save: `<svg viewBox="0 0 16 16"><path fill="#1976d2" d="M2 1h10l3 3v11H2V1zm2 1v4h7V2H4zm1 7v5h6V9H5z"/></svg>`,
    saveAll: `<svg viewBox="0 0 16 16"><path fill="#1565c0" d="M1 3h8l2 2v9H1V3z"/><path fill="#42a5f5" d="M4 1h8l3 3v10H4V1z"/></svg>`,
    search: `<svg viewBox="0 0 16 16"><path fill="none" stroke="currentColor" stroke-width="2" d="M6.5 11a4.5 4.5 0 100-9 4.5 4.5 0 000 9zm3.5-1.5l4 4"/></svg>`,
    collapse: `<svg viewBox="0 0 16 16"><path fill="currentColor" d="M2 4h12v2H2zm3 4h6v2H5zm2 4h2v2H7z"/></svg>`,
    menuDots: `<svg viewBox="0 0 16 16"><circle cx="8" cy="3" r="1.5" fill="currentColor"/><circle cx="8" cy="8" r="1.5" fill="currentColor"/><circle cx="8" cy="13" r="1.5" fill="currentColor"/></svg>`,
    theme: `<svg viewBox="0 0 16 16"><circle cx="8" cy="8" r="4" fill="currentColor"/><path stroke="currentColor" stroke-width="1.5" d="M8 1v2m0 10v2M1 8h2m10 0h2m-2.5-4.5l-1.5 1.5m-7 7l-1.5 1.5m0-10l1.5 1.5m7 7l1.5 1.5"/></svg>`,
    fullscreen: `<svg viewBox="0 0 16 16"><path fill="none" stroke="currentColor" stroke-width="1.5" d="M2 6V2h4m4 0h4v4m0 4v4h-4m-4 0H2v-4"/></svg>`
  };

  // Initialize Workbench
  window.addEventListener('DOMContentLoaded', () => {
    allPrograms = window.JAVA_PROGRAMS || [];
    initThemes();
    buildPackageExplorer(allPrograms);
    initMenuInteractions();
    initToolbar();
    initQuickAccess();
    initSearchModal();
    initEditorTabs();
    initBottomViews();
    initWindowControls();
    initShortcuts();

    // Open first program by default (Experiment 1: ForDemo.java)
    if (allPrograms.length > 0) {
      openProgram(allPrograms[0].id);
    }

    updateStatusBarCounts();
  });

  // =========================================================================
  // Theme Engine (Eclipse Dark vs Classic Light)
  // =========================================================================
  function initThemes() {
    const savedTheme = localStorage.getItem('eclipse_theme') || 'dark';
    if (savedTheme === 'light') {
      document.body.classList.add('theme-light');
    }
  }

  function toggleTheme() {
    document.body.classList.toggle('theme-light');
    const isLight = document.body.classList.contains('theme-light');
    localStorage.setItem('eclipse_theme', isLight ? 'light' : 'dark');
    showToast(isLight ? 'Switched to Eclipse Light (Classic)' : 'Switched to Eclipse Dark', 'info');
  }

  // =========================================================================
  // Package Explorer Tree Generation
  // =========================================================================
  function buildPackageExplorer(programs, filterText = '') {
    const container = document.getElementById('package-tree');
    if (!container) return;
    container.innerHTML = '';

    // Group by Project -> Package -> Files
    const projectsMap = {};
    const normFilter = filterText.toLowerCase().trim();

    programs.forEach(prog => {
      const matchFilter = !normFilter || 
        prog.fileName.toLowerCase().includes(normFilter) ||
        prog.title.toLowerCase().includes(normFilter) ||
        prog.className.toLowerCase().includes(normFilter) ||
        prog.tags.some(t => t.toLowerCase().includes(normFilter)) ||
        (prog.code && prog.code.toLowerCase().includes(normFilter));

      if (filterText && !matchFilter) return;

      const projName = prog.project;
      const pkgName = prog.package;

      if (!projectsMap[projName]) projectsMap[projName] = {};
      if (!projectsMap[projName][pkgName]) projectsMap[projName][pkgName] = [];
      projectsMap[projName][pkgName].push(prog);
    });

    const projectNames = Object.keys(projectsMap).sort();

    if (projectNames.length === 0) {
      container.innerHTML = `
        <div style="padding: 16px; color: var(--sidebar-text-muted); text-align: center;">
          No matching Java files found.<br>
          <span style="font-size: 10px;">Clear filter or try another keyword.</span>
        </div>`;
      return;
    }

    projectNames.forEach(projName => {
      const projsPackages = projectsMap[projName];
      let projTotalFiles = 0;
      Object.values(projsPackages).forEach(arr => projTotalFiles += arr.length);

      // Project Node
      const projNode = document.createElement('div');
      projNode.className = 'tree-item-group';

      const projHeader = document.createElement('div');
      projHeader.className = 'tree-node level-0';
      projHeader.innerHTML = `
        <span class="tree-toggle expanded">▶</span>
        <span class="tree-icon">${ICONS.project}</span>
        <span class="tree-label">${projName}</span>
        <span class="tree-badge">${projTotalFiles}</span>
      `;

      const projChildren = document.createElement('div');
      projChildren.className = 'tree-children open';

      // 'src' virtual folder
      const srcNode = document.createElement('div');
      srcNode.className = 'tree-node level-1';
      srcNode.innerHTML = `
        <span class="tree-toggle expanded">▶</span>
        <span class="tree-icon">${ICONS.srcFolder}</span>
        <span class="tree-label">src</span>
      `;

      const srcChildren = document.createElement('div');
      srcChildren.className = 'tree-children open';

      // Packages
      const packageNames = Object.keys(projsPackages).sort();
      packageNames.forEach(pkgName => {
        const fileList = projsPackages[pkgName];
        const pkgNode = document.createElement('div');
        pkgNode.className = 'tree-node level-2';
        pkgNode.innerHTML = `
          <span class="tree-toggle expanded">▶</span>
          <span class="tree-icon">${ICONS.package}</span>
          <span class="tree-label">${pkgName}</span>
          <span class="tree-badge">${fileList.length}</span>
        `;

        const pkgChildren = document.createElement('div');
        pkgChildren.className = 'tree-children open';

        // Files
        fileList.forEach(prog => {
          const isInterface = prog.code.includes('interface ' + prog.className);
          const fileIcon = isInterface ? ICONS.javaInterface : ICONS.javaClass;

          const fileNode = document.createElement('div');
          fileNode.className = `tree-node level-3 file-item ${prog.id === activeProgramId ? 'selected' : ''}`;
          fileNode.setAttribute('data-id', prog.id);
          fileNode.title = `${prog.title}\nDouble-click or click to open.`;
          fileNode.innerHTML = `
            <span style="width: 12px; display: inline-block;"></span>
            <span class="tree-icon">${fileIcon}</span>
            <span class="tree-label">${prog.fileName}</span>
            <span class="tree-badge">${prog.experimentNo || ''}</span>
          `;

          fileNode.addEventListener('click', () => {
            document.querySelectorAll('.file-item').forEach(el => el.classList.remove('selected'));
            fileNode.classList.add('selected');
            openProgram(prog.id);
          });

          // Right-click context menu
          fileNode.addEventListener('contextmenu', (e) => {
            e.preventDefault();
            copyProgramCode(prog);
          });

          pkgChildren.appendChild(fileNode);
        });

        // Toggle Package collapse
        pkgNode.querySelector('.tree-toggle').addEventListener('click', (e) => {
          e.stopPropagation();
          const toggle = pkgNode.querySelector('.tree-toggle');
          toggle.classList.toggle('expanded');
          pkgChildren.classList.toggle('open');
        });

        srcChildren.appendChild(pkgNode);
        srcChildren.appendChild(pkgChildren);
      });

      // Toggle src collapse
      srcNode.querySelector('.tree-toggle').addEventListener('click', (e) => {
        e.stopPropagation();
        const toggle = srcNode.querySelector('.tree-toggle');
        toggle.classList.toggle('expanded');
        srcChildren.classList.toggle('open');
      });

      projChildren.appendChild(srcNode);
      projChildren.appendChild(srcChildren);

      // Add realistic JRE System Library node
      const jreNode = document.createElement('div');
      jreNode.className = 'tree-node level-1';
      jreNode.innerHTML = `
        <span class="tree-toggle">▶</span>
        <span class="tree-icon">${ICONS.library}</span>
        <span class="tree-label">JRE System Library [JavaSE-17]</span>
      `;
      projChildren.appendChild(jreNode);

      // If JDBC project, add mysql connector jar
      if (projName.includes('JDBC')) {
        const jarNode = document.createElement('div');
        jarNode.className = 'tree-node level-1';
        jarNode.innerHTML = `
          <span style="width: 12px; display: inline-block;"></span>
          <span class="tree-icon">${ICONS.jar}</span>
          <span class="tree-label">mysql-connector-j-8.0.33.jar</span>
        `;
        projChildren.appendChild(jarNode);
      }

      // Toggle Project collapse
      projHeader.querySelector('.tree-toggle').addEventListener('click', (e) => {
        e.stopPropagation();
        const toggle = projHeader.querySelector('.tree-toggle');
        toggle.classList.toggle('expanded');
        projChildren.classList.toggle('open');
      });

      projNode.appendChild(projHeader);
      projNode.appendChild(projChildren);
      container.appendChild(projNode);
    });
  }

  // =========================================================================
  // Program Opening & Tabs Manager
  // =========================================================================
  function openProgram(progId) {
    const prog = allPrograms.find(p => p.id === progId);
    if (!prog) return;

    activeProgramId = progId;

    // Add to open tabs if not already present
    if (!openTabs.includes(progId)) {
      openTabs.push(progId);
    }

    renderTabs();
    renderEditorContent(prog);
    renderOutline(prog);
    renderJavadocInfo(prog);
    updateBreadcrumbs(prog);
    updateTitleBar(prog);

    // Run simulation automatically in Console
    simulateConsoleRun(prog, false);

    // Highlight in package explorer
    document.querySelectorAll('.file-item').forEach(el => {
      if (el.getAttribute('data-id') === progId) {
        el.classList.add('selected');
        el.scrollIntoView({ block: 'nearest' });
      } else {
        el.classList.remove('selected');
      }
    });
  }

  function closeTab(progId, e) {
    if (e) e.stopPropagation();
    const index = openTabs.indexOf(progId);
    if (index === -1) return;

    openTabs.splice(index, 1);

    if (activeProgramId === progId) {
      if (openTabs.length > 0) {
        const newActiveId = openTabs[Math.max(0, index - 1)];
        openProgram(newActiveId);
      } else {
        activeProgramId = null;
        renderTabs();
        clearEditor();
      }
    } else {
      renderTabs();
    }
  }

  function renderTabs() {
    const tabsContainer = document.getElementById('editor-tabs');
    if (!tabsContainer) return;
    tabsContainer.innerHTML = '';

    openTabs.forEach(id => {
      const prog = allPrograms.find(p => p.id === id);
      if (!prog) return;

      const isInterface = prog.code.includes('interface ' + prog.className);
      const icon = isInterface ? ICONS.javaInterface : ICONS.javaClass;

      const tab = document.createElement('div');
      tab.className = `editor-tab ${id === activeProgramId ? 'active' : ''}`;
      tab.title = `${prog.project}/${prog.package}/${prog.fileName}`;
      tab.innerHTML = `
        <span class="tab-icon">${icon}</span>
        <span>${prog.fileName}</span>
        <span class="tab-close" title="Close (Ctrl+W)">×</span>
      `;

      tab.addEventListener('click', () => openProgram(id));
      tab.querySelector('.tab-close').addEventListener('click', (e) => closeTab(id, e));

      tabsContainer.appendChild(tab);
    });
  }

  function clearEditor() {
    const codeWrapper = document.getElementById('code-content');
    const gutter = document.getElementById('code-gutter');
    if (codeWrapper) codeWrapper.innerHTML = '<div style="color: var(--sidebar-text-muted); padding: 20px;">No editor open. Select a file from Package Explorer or press Ctrl+Shift+R to search.</div>';
    if (gutter) gutter.innerHTML = '';
    const breadcrumb = document.getElementById('breadcrumbs-bar');
    if (breadcrumb) breadcrumb.innerHTML = '';
  }

  // =========================================================================
  // Editor Code Rendering & Java Syntax Highlighting
  // =========================================================================
  function renderEditorContent(prog) {
    const gutter = document.getElementById('code-gutter');
    const codeWrapper = document.getElementById('code-content');
    if (!gutter || !codeWrapper) return;

    const lines = prog.code.split('\n');
    gutter.innerHTML = '';
    codeWrapper.innerHTML = '';

    const pre = document.createElement('pre');

    lines.forEach((lineText, idx) => {
      const lineNum = idx + 1;
      const bpKey = `${prog.id}:${lineNum}`;

      // Gutter Line
      const gLine = document.createElement('div');
      gLine.className = `gutter-line ${breakpoints.has(bpKey) ? 'breakpoint' : ''}`;
      gLine.textContent = lineNum;
      gLine.title = `Line ${lineNum} (Click to toggle Breakpoint)`;
      gLine.addEventListener('click', () => {
        if (breakpoints.has(bpKey)) {
          breakpoints.delete(bpKey);
          gLine.classList.remove('breakpoint');
          showToast(`Breakpoint removed at line ${lineNum}`, 'info');
        } else {
          breakpoints.add(bpKey);
          gLine.classList.add('breakpoint');
          showToast(`Breakpoint set at line ${lineNum}`, 'info');
        }
      });
      gutter.appendChild(gLine);

      // Highlighted Code Line
      const cLine = document.createElement('span');
      cLine.className = 'code-line';
      cLine.innerHTML = highlightJavaTokens(lineText) || ' ';
      pre.appendChild(cLine);
    });

    codeWrapper.appendChild(pre);

    // Sync scrolling of gutter and code content
    codeWrapper.onscroll = () => {
      gutter.scrollTop = codeWrapper.scrollTop;
    };
  }

  function highlightJavaTokens(codeLine) {
    if (!codeLine) return '';

    // Handle full-line comments or trailing comments
    const commentIdx = codeLine.indexOf('//');
    if (commentIdx !== -1) {
      const beforeComment = codeLine.substring(0, commentIdx);
      const commentPart = codeLine.substring(commentIdx);
      return highlightJavaTokens(beforeComment) + `<span class="tok-comment">${escapeHtml(commentPart)}</span>`;
    }

    if (codeLine.trim().startsWith('/*') || codeLine.trim().startsWith('*')) {
      return `<span class="tok-comment">${escapeHtml(codeLine)}</span>`;
    }

    // Escape HTML first
    let escaped = escapeHtml(codeLine);

    // Highlighting Strings
    escaped = escaped.replace(/(["'])(?:(?=(\\?))\2.)*?\1/g, '<span class="tok-str">$&</span>');

    // Highlighting Annotations
    escaped = escaped.replace(/@([A-Za-z0-9_]+)/g, '<span class="tok-annotation">@$1</span>');

    // Highlighting Keywords
    const keywords = [
      'abstract', 'boolean', 'break', 'byte', 'case', 'catch', 'char', 'class',
      'const', 'continue', 'default', 'do', 'double', 'else', 'enum', 'extends',
      'final', 'finally', 'float', 'for', 'goto', 'if', 'implements', 'import',
      'instanceof', 'int', 'interface', 'long', 'native', 'new', 'package',
      'private', 'protected', 'public', 'return', 'short', 'static', 'strictfp',
      'super', 'switch', 'synchronized', 'this', 'throw', 'throws', 'transient',
      'try', 'void', 'volatile', 'while', 'true', 'false', 'null'
    ];
    const kwRegex = new RegExp('\\b(' + keywords.join('|') + ')\\b', 'g');
    escaped = escaped.replace(kwRegex, '<span class="tok-kw">$1</span>');

    // Highlighting Common Types / Classes
    const types = [
      'String', 'System', 'Scanner', 'Connection', 'Statement', 'PreparedStatement',
      'ResultSet', 'DriverManager', 'Thread', 'Random', 'File', 'BufferedReader',
      'FileReader', 'InputStreamReader', 'Hashtable', 'Frame', 'JFrame', 'JButton',
      'JTextField', 'JLabel', 'JPanel', 'JScrollPane', 'JRadioButton', 'ButtonGroup',
      'Color', 'Font', 'Graphics', 'ActionEvent', 'ActionListener', 'MouseEvent',
      'MouseListener', 'JOptionPane', 'Applet', 'Exception', 'ArithmeticException',
      'NumberFormatException', 'ArrayIndexOutOfBoundsException', 'FileNotFoundException',
      'IOException', 'Math', 'List', 'ArrayList', 'Node', 'DoublyLinkedList',
      'Person', 'Animal', 'Dog', 'Cat', 'Car', 'Bike', 'Vehicle', 'Shape', 'Rectangle',
      'Triangle', 'Circle', 'Parent', 'Child', 'Father', 'Mother'
    ];
    const typeRegex = new RegExp('\\b(' + types.join('|') + ')\\b', 'g');
    escaped = escaped.replace(typeRegex, '<span class="tok-type">$1</span>');

    // Numbers
    escaped = escaped.replace(/\b(\d+(\.\d+)?)\b/g, '<span class="tok-num">$1</span>');

    return escaped;
  }

  function escapeHtml(text) {
    const map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' };
    return text.replace(/[&<>"']/g, m => map[m]);
  }

  // =========================================================================
  // ONE-CLICK COPY CODE FUNCTIONALITY
  // =========================================================================
  window.copyCurrentProgram = function () {
    const prog = allPrograms.find(p => p.id === activeProgramId);
    if (!prog) {
      showToast('No active program selected to copy.', 'error');
      return;
    }
    copyProgramCode(prog);
  };

  function copyProgramCode(prog) {
    if (!prog || !prog.code) return;

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(prog.code)
        .then(() => {
          showCopySuccess(prog);
        })
        .catch(err => {
          fallbackCopyText(prog.code);
          showCopySuccess(prog);
        });
    } else {
      fallbackCopyText(prog.code);
      showCopySuccess(prog);
    }
  }

  function fallbackCopyText(text) {
    const textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.position = 'fixed';
    textArea.style.left = '-9999px';
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    try {
      document.execCommand('copy');
    } catch (err) {}
    document.body.removeChild(textArea);
  }

  function showCopySuccess(prog) {
    const copyBtn = document.getElementById('editor-copy-btn');
    if (copyBtn) {
      const origHtml = copyBtn.innerHTML;
      copyBtn.innerHTML = `✓ Copied!`;
      copyBtn.style.background = '#2e7d32';
      setTimeout(() => {
        copyBtn.innerHTML = origHtml;
        copyBtn.style.background = '';
      }, 1600);
    }

    showToast(`✓ Copied ${prog.fileName} to clipboard! Ready to paste into Eclipse or compiler.`, 'success');
    updateStatusBarStatus(`Copied ${prog.fileName} (${prog.code.split('\n').length} lines)`);
  }

  // =========================================================================
  // Console & Run Simulation
  // =========================================================================
  function simulateConsoleRun(prog, announce = true) {
    const consoleOutput = document.getElementById('console-output');
    if (!consoleOutput) return;

    const timeStr = new Date().toLocaleTimeString();
    const javaHeader = `&lt;terminated, exit value: 0&gt; ${prog.className} [Java Application] C:\\Program Files\\Java\\jdk-17\\bin\\javaw.exe (${timeStr})`;

    consoleOutput.innerHTML = `
      <div class="console-header-line">
        <span class="console-terminated">&lt;terminated&gt;</span> 
        <span class="console-appname">${prog.className}</span> [Java Application] 
        <span>C:\\Program Files\\Java\\jdk-17\\bin\\javaw.exe</span> (${timeStr})
      </div>
      <div class="console-output-text">${escapeHtml(prog.output || 'Program compiled and executed successfully with no errors.')}</div>
    `;

    if (announce) {
      switchBottomTab('console');
      showToast(`Running ${prog.className} in Eclipse Console...`, 'info');
    }
  }

  window.runCurrentProgram = function () {
    const prog = allPrograms.find(p => p.id === activeProgramId);
    if (!prog) return;
    simulateConsoleRun(prog, true);
  };

  window.debugCurrentProgram = function () {
    const prog = allPrograms.find(p => p.id === activeProgramId);
    if (!prog) return;
    switchBottomTab('console');
    const consoleOutput = document.getElementById('console-output');
    const timeStr = new Date().toLocaleTimeString();
    consoleOutput.innerHTML = `
      <div class="console-header-line">
        <span style="color: #ffb74d;">[Debugging]</span> 
        <span class="console-appname">${prog.className}</span> [Java Application] 
        Connecting to JDWP agent on port 8000... (${timeStr})
      </div>
      <div style="color: #81c784;">Debugger connected. Virtual machine started.</div>
      <div class="console-output-text">${escapeHtml(prog.output || 'Program paused at entry point.')}</div>
    `;
    showToast(`Debugging ${prog.className}... (Breakpoint hit)`, 'info');
  };

  window.copyConsoleOutput = function () {
    const prog = allPrograms.find(p => p.id === activeProgramId);
    if (!prog) return;
    const text = prog.output || 'No output';
    fallbackCopyText(text);
    showToast('✓ Console output copied to clipboard!', 'success');
  };

  window.clearConsole = function () {
    const consoleOutput = document.getElementById('console-output');
    if (consoleOutput) consoleOutput.innerHTML = '<div style="color: var(--sidebar-text-muted);">Console cleared.</div>';
  };

  // =========================================================================
  // Download .java File
  // =========================================================================
  window.downloadCurrentFile = function () {
    const prog = allPrograms.find(p => p.id === activeProgramId);
    if (!prog) return;

    const blob = new Blob([prog.code], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = prog.fileName;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    showToast(`Downloaded ${prog.fileName}`, 'success');
  };

  // =========================================================================
  // Quick Access Search Bar (Toolbar)
  // =========================================================================
  function initQuickAccess() {
    const input = document.getElementById('quick-access-input');
    const dropdown = document.getElementById('quick-access-dropdown');
    if (!input || !dropdown) return;

    input.addEventListener('input', () => {
      const q = input.value.toLowerCase().trim();
      if (!q) {
        dropdown.classList.remove('show');
        return;
      }

      const matches = allPrograms.filter(p => 
        p.fileName.toLowerCase().includes(q) ||
        p.className.toLowerCase().includes(q) ||
        p.title.toLowerCase().includes(q) ||
        p.tags.some(t => t.toLowerCase().includes(q)) ||
        (p.code && p.code.toLowerCase().includes(q))
      );

      if (matches.length === 0) {
        dropdown.innerHTML = `<div style="padding: 10px; color: var(--sidebar-text-muted); font-size: 11px;">No programs found matching "${escapeHtml(q)}"</div>`;
      } else {
        dropdown.innerHTML = `
          <div class="quick-result-category">Matching Java Elements (${matches.length})</div>
        `;
        matches.slice(0, 15).forEach((p, i) => {
          const item = document.createElement('div');
          item.className = `quick-result-item ${i === 0 ? 'selected' : ''}`;
          item.innerHTML = `
            <span class="tree-icon">${ICONS.javaClass}</span>
            <div>
              <div class="item-title">${p.fileName}</div>
              <div style="font-size: 10px; color: var(--sidebar-text-muted);">${p.title}</div>
            </div>
            <div class="item-sub">${p.package}</div>
          `;
          item.addEventListener('click', () => {
            openProgram(p.id);
            dropdown.classList.remove('show');
            input.value = '';
          });
          dropdown.appendChild(item);
        });
      }

      dropdown.classList.add('show');
    });

    input.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        dropdown.classList.remove('show');
        input.blur();
      } else if (e.key === 'Enter') {
        const selected = dropdown.querySelector('.quick-result-item.selected') || dropdown.querySelector('.quick-result-item');
        if (selected) {
          selected.click();
        }
      }
    });

    // Close when clicking outside
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.quick-access-box')) {
        dropdown.classList.remove('show');
      }
    });
  }

  // =========================================================================
  // Package Explorer Filter Input
  // =========================================================================
  const filterInput = document.getElementById('package-filter-input');
  if (filterInput) {
    filterInput.addEventListener('input', () => {
      buildPackageExplorer(allPrograms, filterInput.value);
    });
  }

  // =========================================================================
  // Full Eclipse Search Modal Dialog (Ctrl+H / Ctrl+Shift+R)
  // =========================================================================
  function initSearchModal() {
    const modal = document.getElementById('search-modal');
    const input = document.getElementById('modal-search-input');
    const resultsContainer = document.getElementById('modal-results-list');
    const openBtn = document.getElementById('modal-open-btn');
    const cancelBtn = document.getElementById('modal-cancel-btn');

    let selectedProgId = null;

    window.openSearchModal = function () {
      modal.classList.add('open');
      input.value = '';
      input.focus();
      renderModalResults('');
    };

    window.closeSearchModal = function () {
      modal.classList.remove('open');
    };

    if (cancelBtn) cancelBtn.addEventListener('click', closeSearchModal);

    if (input) {
      input.addEventListener('input', () => {
        renderModalResults(input.value);
      });

      input.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
          closeSearchModal();
        } else if (e.key === 'Enter') {
          if (selectedProgId) {
            openProgram(selectedProgId);
            closeSearchModal();
          }
        }
      });
    }

    if (openBtn) {
      openBtn.addEventListener('click', () => {
        if (selectedProgId) {
          openProgram(selectedProgId);
          closeSearchModal();
        }
      });
    }

    function renderModalResults(q) {
      const norm = q.toLowerCase().trim();
      const matches = !norm ? allPrograms : allPrograms.filter(p =>
        p.fileName.toLowerCase().includes(norm) ||
        p.className.toLowerCase().includes(norm) ||
        p.title.toLowerCase().includes(norm) ||
        p.tags.some(t => t.toLowerCase().includes(norm)) ||
        (p.code && p.code.toLowerCase().includes(norm))
      );

      resultsContainer.innerHTML = '';

      if (matches.length === 0) {
        resultsContainer.innerHTML = `<div style="padding: 14px; color: var(--sidebar-text-muted);">No matches found for "${escapeHtml(q)}"</div>`;
        selectedProgId = null;
        return;
      }

      selectedProgId = matches[0].id;

      matches.forEach((p, idx) => {
        const row = document.createElement('div');
        row.className = `modal-result-row ${idx === 0 ? 'selected' : ''}`;
        row.innerHTML = `
          <span class="tree-icon">${ICONS.javaClass}</span>
          <span style="font-weight: 600;">${p.fileName}</span>
          <span style="color: var(--sidebar-text-muted); font-size: 11px;">- ${p.title}</span>
          <span class="res-path">${p.project}/${p.package}</span>
        `;

        row.addEventListener('click', () => {
          resultsContainer.querySelectorAll('.modal-result-row').forEach(r => r.classList.remove('selected'));
          row.classList.add('selected');
          selectedProgId = p.id;
        });

        row.addEventListener('dblclick', () => {
          openProgram(p.id);
          closeSearchModal();
        });

        resultsContainer.appendChild(row);
      });
    }
  }

  // =========================================================================
  // Outline View Generator
  // =========================================================================
  function renderOutline(prog) {
    const outlineContainer = document.getElementById('outline-content');
    if (!outlineContainer) return;

    outlineContainer.innerHTML = `
      <div class="tree-node level-0" style="padding-left: 6px;">
        <span class="tree-icon">${ICONS.package}</span>
        <span class="tree-label">${prog.package}</span>
      </div>
      <div class="tree-node level-1" style="padding-left: 18px; font-weight: 600;">
        <span class="tree-icon">${ICONS.javaClass}</span>
        <span class="tree-label">${prog.className}</span>
      </div>
    `;

    // Extract methods dynamically with regex
    const methodMatches = prog.code.matchAll(/(public|protected|private|static|\s)+[\w<>\[\]]+\s+(\w+)\s*\([^)]*\)\s*(?:throws\s+[\w,\s]+)?\s*\{/g);
    for (const match of methodMatches) {
      const methodName = match[2];
      if (['if', 'for', 'while', 'switch', 'catch'].includes(methodName)) continue;

      const mNode = document.createElement('div');
      mNode.className = 'tree-node level-2';
      mNode.style.paddingLeft = '30px';
      mNode.innerHTML = `
        <span class="tree-icon">${ICONS.method}</span>
        <span class="tree-label">${methodName}()</span>
      `;
      outlineContainer.appendChild(mNode);
    }
  }

  // =========================================================================
  // Javadoc / Info Tab
  // =========================================================================
  function renderJavadocInfo(prog) {
    const javadocContainer = document.getElementById('javadoc-content');
    if (!javadocContainer) return;

    javadocContainer.innerHTML = `
      <h3>${prog.title}</h3>
      <p style="margin-bottom: 8px;"><strong>Source:</strong> ${prog.sourcePdf} &nbsp;|&nbsp; <strong>Package:</strong> <code>${prog.package}</code> &nbsp;|&nbsp; <strong>Main Class:</strong> <code>${prog.className}</code></p>
      <div style="background: rgba(255, 255, 255, 0.05); padding: 8px 12px; border-radius: 4px; border-left: 3px solid #007acc; margin-bottom: 10px;">
        <strong>Problem Statement / Description:</strong><br>
        ${escapeHtml(prog.description)}
      </div>
      <div>
        <strong>Key Concepts & Keywords:</strong>
        <div class="javadoc-tag-list">
          ${prog.tags.map(t => `<span class="javadoc-tag">${t}</span>`).join('')}
        </div>
      </div>
      <div style="margin-top: 12px;">
        <button onclick="window.copyCurrentProgram()" class="copy-code-btn" style="display: inline-flex; font-size: 11px;">
          ${ICONS.copy} Copy Java Code
        </button>
        <button onclick="window.runCurrentProgram()" class="action-btn" style="display: inline-flex; margin-left: 6px;">
          ${ICONS.run} Run Program
        </button>
      </div>
    `;
  }

  // =========================================================================
  // Navigation & Breadcrumbs
  // =========================================================================
  function updateBreadcrumbs(prog) {
    const bc = document.getElementById('breadcrumbs-bar');
    if (!bc) return;
    bc.innerHTML = `
      <span class="breadcrumb-item">${prog.project}</span> &gt;
      <span class="breadcrumb-item">src</span> &gt;
      <span class="breadcrumb-item">${prog.package}</span> &gt;
      <span class="breadcrumb-item active">${prog.fileName}</span> &gt;
      <span class="breadcrumb-item">${prog.className}</span>
    `;
  }

  function updateTitleBar(prog) {
    const title = document.getElementById('workbench-title');
    if (title && prog) {
      title.textContent = `workspace - Java - ${prog.project}/src/${prog.package.replace(/\./g, '/')}/${prog.fileName} - Eclipse IDE`;
    }
  }

  function updateStatusBarStatus(msg) {
    const el = document.getElementById('status-msg');
    if (el) el.textContent = msg;
  }

  function updateStatusBarCounts() {
    const countEl = document.getElementById('status-file-count');
    if (countEl) countEl.textContent = `${allPrograms.length} Java Files Available`;
  }

  // =========================================================================
  // Bottom Panel Tab Switching
  // =========================================================================
  function initBottomViews() {
    document.querySelectorAll('.bottom-tab').forEach(tab => {
      tab.addEventListener('click', () => {
        const target = tab.getAttribute('data-tab');
        switchBottomTab(target);
      });
    });
  }

  function switchBottomTab(tabName) {
    activeBottomTab = tabName;
    document.querySelectorAll('.bottom-tab').forEach(tab => {
      tab.classList.toggle('active', tab.getAttribute('data-tab') === tabName);
    });

    document.querySelectorAll('.bottom-view-content').forEach(view => {
      view.style.display = view.getAttribute('data-tab-content') === tabName ? 'block' : 'none';
    });
  }

  // =========================================================================
  // Menu Interactions
  // =========================================================================
  function initMenuInteractions() {
    const menuItems = document.querySelectorAll('.menu-item');
    menuItems.forEach(item => {
      item.addEventListener('click', (e) => {
        e.stopPropagation();
        const wasActive = item.classList.contains('active');
        menuItems.forEach(m => m.classList.remove('active'));
        if (!wasActive) item.classList.add('active');
      });
    });

    document.addEventListener('click', () => {
      menuItems.forEach(m => m.classList.remove('active'));
    });
  }

  // =========================================================================
  // Toolbar Buttons
  // =========================================================================
  function initToolbar() {
    const themeBtn = document.getElementById('tb-theme-toggle');
    if (themeBtn) themeBtn.addEventListener('click', toggleTheme);

    const fullBtn = document.getElementById('tb-fullscreen-toggle');
    if (fullBtn) fullBtn.addEventListener('click', toggleFullscreen);

    const searchBtn = document.getElementById('tb-search-btn');
    if (searchBtn) searchBtn.addEventListener('click', openSearchModal);

    const runBtn = document.getElementById('tb-run-btn');
    if (runBtn) runBtn.addEventListener('click', runCurrentProgram);

    const debugBtn = document.getElementById('tb-debug-btn');
    if (debugBtn) debugBtn.addEventListener('click', debugCurrentProgram);

    const saveBtn = document.getElementById('tb-save-btn');
    if (saveBtn) saveBtn.addEventListener('click', () => showToast('Saved file to local Eclipse workspace.', 'info'));
  }

  // =========================================================================
  // Window Controls & Fullscreen (Stealth Mode)
  // =========================================================================
  function initWindowControls() {
    const fsBtn = document.getElementById('win-btn-max');
    if (fsBtn) fsBtn.addEventListener('click', toggleFullscreen);

    const minBtn = document.getElementById('win-btn-min');
    if (minBtn) minBtn.addEventListener('click', () => showToast('Minimized to Taskbar', 'info'));

    const closeBtn = document.getElementById('win-btn-close');
    if (closeBtn) closeBtn.addEventListener('click', () => {
      if (confirm('Exit Eclipse IDE?')) {
        window.close();
      }
    });
  }

  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(err => {});
      showToast('Entered Fullscreen Stealth Mode (Press Esc or F11 to exit)', 'info');
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen().catch(err => {});
      }
    }
  }

  // =========================================================================
  // Keyboard Shortcuts
  // =========================================================================
  function initShortcuts() {
    window.addEventListener('keydown', (e) => {
      // Ctrl+Shift+R or Ctrl+H -> Open Search Modal
      if ((e.ctrlKey && e.shiftKey && (e.key === 'R' || e.key === 'r')) || (e.ctrlKey && (e.key === 'h' || e.key === 'H'))) {
        e.preventDefault();
        openSearchModal();
      }
      // Ctrl+3 -> Focus Quick Access Search
      else if (e.ctrlKey && e.key === '3') {
        e.preventDefault();
        const qaInput = document.getElementById('quick-access-input');
        if (qaInput) qaInput.focus();
      }
      // Alt+C -> Copy Code
      else if (e.altKey && (e.key === 'c' || e.key === 'C')) {
        e.preventDefault();
        copyCurrentProgram();
      }
      // Ctrl+F11 -> Run
      else if (e.ctrlKey && e.key === 'F11') {
        e.preventDefault();
        runCurrentProgram();
      }
      // F11 -> Toggle Fullscreen
      else if (e.key === 'F11') {
        e.preventDefault();
        toggleFullscreen();
      }
      // Ctrl+W -> Close Tab
      else if (e.ctrlKey && (e.key === 'w' || e.key === 'W')) {
        e.preventDefault();
        if (activeProgramId) closeTab(activeProgramId);
      }
    });
  }

  // =========================================================================
  // Toast Notification
  // =========================================================================
  let toastTimer = null;
  function showToast(message, type = 'info') {
    const toast = document.getElementById('eclipse-toast');
    if (!toast) return;

    toast.textContent = message;
    toast.className = `eclipse-toast show ${type}`;

    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      toast.classList.remove('show');
    }, 2800);
  }

  // =========================================================================
  // Panel Resizers
  // =========================================================================
  const sidebar = document.querySelector('.sidebar-panel');
  const resizer = document.querySelector('.resizer');
  if (sidebar && resizer) {
    let isResizing = false;
    resizer.addEventListener('mousedown', (e) => {
      isResizing = true;
      resizer.classList.add('dragging');
      document.body.style.cursor = 'col-resize';
    });

    document.addEventListener('mousemove', (e) => {
      if (!isResizing) return;
      const newWidth = e.clientX;
      if (newWidth > 180 && newWidth < 600) {
        sidebar.style.width = newWidth + 'px';
      }
    });

    document.addEventListener('mouseup', () => {
      if (isResizing) {
        isResizing = false;
        resizer.classList.remove('dragging');
        document.body.style.cursor = '';
      }
    });
  }

  const bottomPanel = document.querySelector('.bottom-view-panel');
  const bottomResizer = document.querySelector('.resizer-horizontal');
  if (bottomPanel && bottomResizer) {
    let isResizingBottom = false;
    bottomResizer.addEventListener('mousedown', () => {
      isResizingBottom = true;
      bottomResizer.classList.add('dragging');
      document.body.style.cursor = 'row-resize';
    });

    document.addEventListener('mousemove', (e) => {
      if (!isResizingBottom) return;
      const newHeight = window.innerHeight - e.clientY - 22; // 22 for status bar
      if (newHeight > 80 && newHeight < 600) {
        bottomPanel.style.height = newHeight + 'px';
      }
    });

    document.addEventListener('mouseup', () => {
      if (isResizingBottom) {
        isResizingBottom = false;
        bottomResizer.classList.remove('dragging');
        document.body.style.cursor = '';
      }
    });
  }

  // Outline / Cheat Sheet Collapsible on Right
  window.toggleRightSidebar = function () {
    const rightPanel = document.getElementById('right-sidebar-panel');
    if (rightPanel) {
      rightPanel.style.display = rightPanel.style.display === 'none' ? 'flex' : 'none';
    }
  };

})();

