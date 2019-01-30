from selenium import webdriver
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", help="File containing the url list")
parser.add_argument("--output", help="The path of the folder for the output files")
parser.add_argument("--webdriver", help="The path of the webdriver binary")
args = parser.parse_args()

file = args.file if args.file else None
output = args.output if args.output else None
driver = args.webdriver if args.webdriver else None

print("\n\n")
print("                   .':l,.    .....'.  .'',,'...........,;;,'..                  ")
print("                     .;oc..,;;'...'....cl:'........'...',,'..                   ")
print("                    ..;loo:,;lo;.....',;c;,'..':,....';'.''.                    ")
print("                    .,coxkx:.,:..,,;:l:...';:,;c;',;loc,....        ...         ")
print("         .           .cxkkd;,::;:;,:do::cc::c;,;cc,,;;,,.           .;;.        ")
print("       ...            .';ll;,::::;:::;,,,:oc,,;cc'':lldx:.         .,::;.       ")
print("       ..             .:;,colcc:,:oc;;::;;;;;ccoo;;codxd,          .':clc,.     ")
print("       .     ..       ,dxc;cdl,:::loc:::;;,;coddo:cocldc.       ...   .':c;.    ")
print("          .....       .:odo::::;';c:;clloc:ccoxoloclodl,.      .,''...  'cc,.   ")
print("     .    ......      ..:oxo;:l;.,c:.':ooc,:lllclcclol:'.      .,,'''....,c:.   ")
print("           .....'''.    .;cc:co::c,'. .:olcc:ccclc;lo:,...,;:ll;;;,'''.. .':,.  ")
print("    .                    ';cc::;,:c::'.,:;:::',ccclol;.  .'.'','.'....... .',.. ")
print("   .             ..       'co:;;',ccloc'..,:;:cccll;.     ....     ........''...")
print("                .;,.       .,oc,;,,:llc;''',;cddc'...     .;c;... .........'',..")
print("              ...,c:,....... .cooc;::;,;c::lodx:  ':c;,'';lol,.,'...............")
print("            ......';::;;,'.    ,lool;'.',,:odo;,...,:cllolc:;:l:'..''...........")
print("             ...''..........   .,cdxdc,:lokko;':ocll:;;;:ccloo:'...''...........")
print("              ......'',;cooc,.....';c:;:ldd:,',lxOO0Odoollol:;',,'''............")
print("      .      ....'',;;;;;:ll;,..'''''ldc;;;;',ldk0K0xoodddddll:;,'.....';,'.....")
print("     ....    ...';;;,''...,c:;,',::,,oOo;::ccclxkOko::ldddoololc;'....,:c;,''...")
print("   .  ....    ..'''',;;;;,',;clc:::,.:d:',clodddk0Oxxxdkkool::lc:;'.';cc::;,'...")
print("        ..    .......',;:cc;;:lollc'.,c,..cddkOkOOO0ko:::;:c::c;,,,',,',,',;,..,")
print("         ........',,...,,.';::cccc;.......:odkkxxxdc;'..;;,;:;:::::;,'...'..''',")
print("           ...'.',,. .....'cdxkxo:.    ....;dO0K0Od:'''''..',;:cc::::,'.........")
print("      .   .....''..  ..   .,;cdxkdl'    ..;x00Okxdl;..... .'''',;;'',;'......   ")
print("           ......     . .... .':loo:.  .'ckOxdl:,,;,''..'..''....''..   ....'.  ")
print("                    .........   .,:l;  ,lool;''.............';,.....      ..';. ")
print("                   ....     ... ....,'':c:'..  .''....'.''.. .',''..',;,..','','")
print("                 ...  .             ..'............  ...',.    .';;',cc:c:;::,..")
print("                 .              ...      ...    ....    ':'..   .....''.:llll:'")
print("                  __      __      ___.    ________         .__   ")
print("                 /  \    /  \ ____\_ |__  \_____  \__  _  _|  |  ")
print("                 \   \/\/   // __ \| __ \  /   |   \ \/ \/ /  |  ")
print("                  \        /\  ___/| \_\ \/    |    \     /|  |__")
print("                   \__/\  /  \___  >___  /\_______  /\/\_/ |____/")
print("                        \/       \/    \/         \/             ")
print("\n                       by Bastian Muhlhauser @xpl0ited1\n\n")


if (file != None and output != None) and driver != None:
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	browser = webdriver.Chrome(driver, chrome_options=options)
	if not os.path.exists(output):
		os.mkdir(output)
	print("[+] Reading file...")
	with open(file) as f:
		lines = f.readlines()
		for line in lines:
			print("[+] Getting screenshots for "+line)
			browser.get('http://'+line)
			print("[+] Saving http_"+line+'.png')
			browser.save_screenshot(output+'/http_'+line+'.png')
			browser.get('https://'+line)
			print("[+] Saving https_"+line+'.jpg')
			browser.save_screenshot(output+'/https_'+line+'.png')
		print("[+] Done.")
		browser.close()

