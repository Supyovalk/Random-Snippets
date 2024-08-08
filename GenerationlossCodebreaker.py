def reverseandremove(str):
    idxseperator=(len(str)//2)+1
    return str[idxseperator:]+str[0:idxseperator-1]
def main():
    print(reverseandremove("wvby-ylqs"))
    lst="'1g525-gla5d' 'g4hdk-gjwer' 'fqmak-nlwhp' 'ggvaw-rbpzh' 'bv3g-6rhv' 'hmhjs-wgujw' 'kbibk-yjyhf' 'hixce-hnyyw' 'mtpfy-grorg' 'fmtu-xvd2' 'oqtbc-xvzke' 'xruxl-bkgtu' 'saana-klgcw' 'iynbn-fpjsu' 'mu9k-bhwp' 'yjvsd-pdgov' 'sdiqx-onnpv' 'llygh-xrbro' '7ya9-ycsu' 'vznq-jdbe' 'hwow-jjuhmf' 'ekkagw-mzyc' 'seada-vuivc' 'dlyhm-uphge' 'mrka-jywc' 'jfibq-udwdo' 'dyehc-lawmd' 'tzuge-omicq' 'yfscy-omheh' 'rctft-nnnmv' 'cabz-7mgd' 'sfvn-v6rh' 'dlyhm-uphge' 'hwow-jjuhmf' 'yjvsd-pdgov'".split(" ")
    lst=[i.replace("'","") for i in lst]
    print(lst)
    print("".join([reverseandremove(i) for i in lst]))
main()