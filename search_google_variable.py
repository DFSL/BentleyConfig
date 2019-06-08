import sublime, sublime_plugin, webbrowser

class SearchGoogleVariableCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		if len(view.sel()) == 1:
			var = view.substr(view.word(view.sel()[0]))
			url = "https://www.google.com/search?q="+var+"+Microstation"
			webbrowser.get().open_new_tab(url)
