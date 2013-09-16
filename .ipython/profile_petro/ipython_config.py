# Configuration file for ipython.
import os.path

c = get_config()

c.TerminalIPythonApp.profile = u'sh'
c.TerminalIPythonApp.display_banner = False
c.TerminalInteractiveShell.editor = 'vim'
c.TerminalInteractiveShell.term_title = True
c.TerminalInteractiveShell.cache_size = 1000
c.TerminalInteractiveShell.pdb = True

c.TerminalIPythonApp.exec_files = [
    os.path.join(
        os.path.expanduser('~'), '.ipython/profile_petro/code.py'
    ),
]
