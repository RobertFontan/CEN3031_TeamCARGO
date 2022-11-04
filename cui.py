import sys

from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.widgets import Frame
from asciimatics.widgets import Layout
from asciimatics.widgets import Button
from asciimatics.widgets import Text
from asciimatics.widgets import CheckBox
from asciimatics.widgets import ListBox
from asciimatics.widgets import Widget
from asciimatics.widgets import Divider
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

class LibraryView(Frame):
	def __init__(self, screen, model):
		super(LibraryView, self).__init__(screen, screen.height, screen.width, on_load=self._reload_list)

		self._model = model
		self._list_view = ListBox(
			Widget.FILL_FRAME,
			[],
			name="books",
			add_scroll_bar=True)

		self._add_button = Button("Add", self._add)
		layout = Layout([100], fill_frame=True)
		self.add_layout(layout)
		layout.add_widget(self._list_view)
		layout.add_widget(Divider())
		layout2 = Layout([1, 1, 1, 1])
		self.add_layout(layout2)
		layout2.add_widget(self._add_button, 0)
		self.fix()
	
	def _reload_list(self, new_value=None):
		books = self._model.get_books()
		self._list_view.options = [(str(books[i]), i) for i in range(len(books))]
		self._list_view.value = new_value
	
	def _add(self):
		self._model.current_id = None
		raise NextScene("isbn_lookup")

class AddBookView(Frame):
	def __init__(self, screen, model):
		super(AddBookView, self).__init__(screen, 5, int(screen.width * 2 // 3), can_scroll=False)

		self._model = model
		layout = Layout([1], True)
		self.add_layout(layout)
		layout.add_widget(Text("ISBN:", "isbn"))
		layout.add_widget(CheckBox("Electronic"))
		
		layout2 = Layout([1, 1, 1, 1])
		self.add_layout(layout2)
		layout2.add_widget(Button("Lookup", self._lookup), 0)
		layout2.add_widget(Button("Cancel", self._cancel), 1)

		self.fix()

	def _lookup(self):
		self.save()
		result = book.lookup_isbn(self.data["isbn"])
		self._model.add_book(result)
		raise NextScene("library")

	def _cancel(self):
		raise NextScene("library")

def ui(screen, scene):
	scenes = [
		Scene([LibraryView(screen, library)], -1, name="library"),
		Scene([AddBookView(screen, library)], -1, name="isbn_lookup")
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