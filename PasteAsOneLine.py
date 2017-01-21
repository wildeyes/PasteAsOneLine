import sublime, sublime_plugin

class PasteAsOneLineCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    execute(self, ' ')

class PasteAsOneLineWithCommasCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    execute(self, ', ')

def execute(self, delimeter):
  # get contents of the clipboard
  clipboard = sublime.get_clipboard()
  # store original clipboard
  original_clipboard = clipboard
  # set the clipboard to the new onelined content
  sublime.set_clipboard(merge_lines(clipboard, delimeter))

  s = sublime.load_settings("ClipboardHistory.sublime-settings")

  if s.get('paste_and_indent'):
    self.view.run_command('paste_and_indent')
  else:
    self.view.run_command('paste')

  #return the original clipboa rd
  sublime.set_clipboard(original_clipboard)

def merge_lines(mergee, delimeter = ' '):
  mergee = mergee.replace('\n', delimeter)
  mergee = mergee.replace('\r', delimeter)
  mergee = mergee.replace('\t', '')
  mergee = mergee.replace('   ', delimeter)
  mergee = mergee.replace('  ', delimeter)
  mergee = mergee.replace('  ', delimeter)
  return mergee