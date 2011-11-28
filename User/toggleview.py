import sublime, sublime_plugin

class ToggleViewCommand(sublime_plugin.WindowCommand):
	def run(self):
		group_idx = (self.window.active_group() + 1) % self.window.num_groups()
		self.window.focus_group(group_idx)
