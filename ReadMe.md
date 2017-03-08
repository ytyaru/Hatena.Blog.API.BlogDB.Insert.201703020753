# このソフトウェアについて

はてなAPIで取得したXMLからブログ情報を取得しDBに保存する。

# 開発環境

* Linux Mint 17.3 MATE
* Firefox 42.0

# 準備

* [はてなブログAPIでエントリを取得する](http://ytyaru.hatenablog.com/entry/2017/06/23)
* [はてなアカウントDBを作る](http://ytyaru.hatenablog.com/entry/2017/06/30/000000)
* [はてなブログDBを作る](http://ytyaru.hatenablog.com/entry/2017/07/01/000000)
* [はてなブログ記事DBを作る](http://ytyaru.hatenablog.com/entry/2017/07/02/000000)

以下のようにmain.pyを変更する。

1. 上記の準備で得たXMLとDBファイルパスを以下のコードで設定する。

```
if __name__ == '__main__':
    client = Scraping(
        "../resource/201702281505/ytyaru.ytyaru.hatenablog.com.Services.xml", 
        "meta_Hatena.Accounts.sqlite3",
        "meta_Hatena.Blogs.sqlite3")
    client.scrape()
```

# 実行

```sh
python3 main.py
```

# 結果

XMLファイルの記事データが、[はてなブログ記事DBを作る](http://ytyaru.hatenablog.com/entry/2017/07/02/000000)で作成したDBに保存される。

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

なお、使用させていただいたライブラリは以下のライセンスである。感謝。

Library|License|Copyright
-------|-------|---------
[xmltodict](https://github.com/martinblech/xmltodict)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (C) 2012 Martin Blech and individual contributors.](https://github.com/martinblech/xmltodict/blob/master/LICENSE)
[requests_oauthlib](https://github.com/requests/requests-oauthlib)|[ISC](https://opensource.org/licenses/ISC)|[Copyright (c) 2014 Kenneth Reitz.](https://github.com/requests/requests-oauthlib/blob/master/LICENSE)
[bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)|[MIT](https://opensource.org/licenses/MIT)|[Copyright © 1996-2011 Leonard Richardson](https://pypi.python.org/pypi/beautifulsoup4),[参考](http://tdoc.info/beautifulsoup/)
[dataset](https://dataset.readthedocs.io/en/latest/)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2013, Open Knowledge Foundation, Friedrich Lindenberg, Gregor Aisch](https://github.com/pudo/dataset/blob/master/LICENSE.txt)

