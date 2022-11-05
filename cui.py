import sys

from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.widgets import Frame, Layout, Button, Text, CheckBox, ListBox, Widget, Divider, PopUpDialog
from asciimatics.exceptions import ResizeScreenError, NextScene

import bookdb, book

# 0374214913
# 0132058405

class LibraryModel(object):
	def __init__(self):
		self.session = bookdb.create_session()
	
	def get_books(self):
		return bookdb.get_books(self.session)
	
	def add_book(self, book):
		return bookdb.add_book(self.session, book)
	
	def remove_book(self, book):
		return bookdb.remove_book(self.session, book.isbn)

class LibraryView(Frame):
	def __init__(self, screen, model):
		super(LibraryView, self).__init__(screen, screen.height, screen.width, on_load=self._reload_list, has_border=False)

		self._model = model
		self._list_view = ListBox(
			Widget.FILL_FRAME,
			[],
			name="books",
			add_scroll_bar=True)

		layout = Layout([100], fill_frame=True)
		self.add_layout(layout)
		layout.add_widget(self._list_view)
		layout.add_widget(Divider())

		layout2 = Layout([1, 1, 1, 1])
		self.add_layout(layout2)
		layout2.add_widget(Button("Add", self._add), 0)
		layout2.add_widget(Button("Remove", self._confirm_remove), 1)
		layout2.add_widget(Button("Quit", self._quit), 3)
		self.fix()
	
	def _reload_list(self, new_value=None):
		self.books = self._model.get_books()
		self._list_view.options = [(str(self.books[i]), i) for i in range(len(self.books))]
		self._list_view.value = new_value
	
	def _add(self):
		self._scene.add_effect(AddBookView(self.screen, self._model, self._reload_list))
	
	def _confirm_remove(self):
		self._scene.add_effect(PopUpDialog(self.screen, "Are you sure you want to remove this book?", ["Remove", "Cancel"], self._remove, True))
	
	def _remove(self, response):
		if (response != 0):
			return
		self._model.remove_book(self.books[self._list_view.value])
		self._reload_list()
	
	def _quit(self):
		sys.exit(0)

class AddBookView(Frame):
	def __init__(self, screen, model, callback):
		super(AddBookView, self).__init__(screen, 5, int(screen.width * 2 // 3), can_scroll=False, is_modal=True, has_shadow=True)

		self._model = model
		self._callback = callback
		layout = Layout([1], True)
		self.add_layout(layout)
		layout.add_widget(Text("ISBN:", "isbn"))
		layout.add_widget(CheckBox("Electronic", name="electronic"))
		
		layout2 = Layout([1, 1, 1, 1])
		self.add_layout(layout2)
		layout2.add_widget(Button("Lookup", self._lookup), 0)
		layout2.add_widget(Button("Cancel", self._cancel), 1)

		self.fix()

	def _lookup(self):
		self.save()
		result = book.lookup_isbn(self.data["isbn"])
		result.electronic = self.data["electronic"]
		self._model.add_book(result)
		self._scene.remove_effect(self)
		self._callback()

	def _cancel(self):
		self._scene.remove_effect(self)

def ui(screen, scene):
	scenes = [
		Scene([LibraryView(screen, library)], -1, name="library"),
	]

	screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)

library = LibraryModel()
last_scene = None
while True:
	try:
		Screen.wrapper(ui, arguments=[last_scene])
		sys.exit(0)
	except ResizeScreenError as e:
		last_scene = e.scene