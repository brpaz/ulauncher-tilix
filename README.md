# ulauncher-tilix

[![Build Status](https://img.shields.io/travis/com/brpaz/ulauncher-tilix.svg)](https://github.com/brpaz/ulauncher-tilix)
[![GitHub license](https://img.shields.io/github/license/brpaz/ulauncher-tilix.svg)](https://github.com/brpaz/:ulauncher-tilix/blob/master/LICENSE)

> Open your saved Tilix sessions from Ulauncher

## Screenshot

![screnshot.png](screenshot.png)

[Demo](demo.gif)

## Requirements

- Ulauncher
- Python >= 2.7
- [Tilix terminal emulator](https://gnunn1.github.io/tilix-web/)

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```
https://github.com/brpaz/ulauncher-tilix
```

## Usage

By default, this extension looks for layout files located in "~/.config/tilix/sessions". You can change it in the extension settings.

Then, open Ulauncher and type "tilix" in the input box. A list of files on your sessions folder will be displayed. selecting one will load a new tilix session based on the save layout.

## Development

```
git clone https://github.com/brpaz/ulauncher-tilix
make link
```

The `make link` command will symlink the cloned repo into the appropriate location on the ulauncher extensions folder.

To see your changes, stop ulauncher and run it from the command line with: `ulauncher -v`.

## Contributing

- Fork it!
- Create your feature branch: git checkout -b my-new-feature
- Commit your changes: git commit -am 'Add some feature'
- Push to the branch: git push origin my-new-feature
- Submit a pull request :D

## License

MIT &copy; [Bruno Paz]
