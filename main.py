""" Main Module """

import logging
import os
import subprocess
# pylint: disable=import-error
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

LOGGING = logging.getLogger(__name__)


class TilixExtension(Extension):
    """ Main Extension Class  """

    def __init__(self):
        """ Initializes the extension """
        super(TilixExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):
    """ Listener that handles the user input """

    # pylint: disable=unused-argument,no-self-use
    def on_event(self, event, extension):
        """ Handles the event """

        query = event.get_argument() or ""

        sessions_path = os.path.expanduser(
            extension.preferences['sessions_dir'])

        if not os.path.isdir(sessions_path):
            return RenderResultListAction([ExtensionResultItem(
                icon='images/icon.png',
                name="The sessions directory does not exist",
                description="Please check your extension settings",
                on_enter=HideWindowAction()
            )])

        sessions = os.listdir(sessions_path)

        if query:
            sessions = list(
                filter(lambda x: query.lower() in x.lower(), sessions))

        if not sessions:
            return RenderResultListAction([ExtensionResultItem(
                icon='images/icon.png',
                name="No Tilix sessions found",
                on_enter=HideWindowAction()
            )])

        items = []
        for session in sessions:
            name = os.path.splitext(os.path.basename(session))[
                0].replace('_', ' ').replace('-', ' ').capitalize()

            data = {"session": session}

            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name=name,
                                             on_enter=ExtensionCustomAction(data)))

        return RenderResultListAction(items)


class ItemEnterEventListener(EventListener):
    """ Listener that handles the click on an item """

    # pylint: disable=unused-argument,no-self-use
    def on_event(self, event, extension):
        """ Handles the event """
        data = event.get_data()

        sessions_path = os.path.expanduser(
            extension.preferences['sessions_dir'])

        file_path = os.path.join(sessions_path, data['session'])
        subprocess.Popen(['tilix --session %s' % file_path], shell=True,
                         stdin=None, stdout=None, stderr=None, close_fds=True)


if __name__ == '__main__':
    TilixExtension().run()
