from Plugins.Plugin import PluginDescriptor
from Screens.MessageBox import MessageBox


def start(session):
    session.open(MessageBox, "Hello World!")


def Plugins(path, **kwargs):
    return [
        PluginDescriptor(name="Example", where=PluginDescriptor.WHERE_PLUGINMENU, fnc=start)
    ]
