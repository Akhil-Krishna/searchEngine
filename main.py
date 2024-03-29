'''A Package which will act as a Search Engine and It is used as a searching interface'''

from time import sleep as s
import sys, wikipedia ,googlesearch,webbrowser,random





def syst(l):
  '''Will output just like manual typing without print'''
  for i in l:
    sys.stdout.write(i)
    sys.stdout.flush()
    s(0.07)
def Search():
  '''Search Engine function'''
  lst=['🅐🅚-🅢🅔🅐🅡🅒🅗', '𝔸𝕂-𝕊𝔼𝔸ℝℂℍ ','🄰🄺-🅂🄴🄰🅁🄲🄷','𝚊𝚔-𝚜𝚎𝚊𝚛𝚌𝚑','ᗩᛕ-ᔕᗴᗩᖇᑕᕼ']
  print('_'*60)
  print('='*60)
  print(' '*22,random.choice(lst))
  #['🅐🅚-🅢🅔🅐🅡🅒🅗', '𝔸𝕂-𝕊𝔼𝔸ℝℂℍ ']
  print('='*60)
  txt=input('𝐀𝐊 : SEARCH HERE        >>> ')

  print()
  l='𝐀𝐊 : Searching...'
  syst(l)
  if 'https' or '.com' in txt:
    webbrowser.open(txt)
  s(1)
  print('')
  result=googlesearch.search(txt)
  try:
    print()
    syst('𝐀𝐊 : \n     '+wikipedia.summary(txt,sentences=5))
    #,features=html.parser))
    print()
    print('='*60)
    s(0.9)
    print()
    l1='𝐀𝐊 : Links are provided ,click on it for more information.. '
    syst(l1)
    print(' '*60)
  except:
    print('='*60)
    syst('𝐀𝐊 : Links are provided,click on it to get the information...')
    print(' '*60)
    print()
  for i in result:
    print('-'*60)
    print(' '*5,i)
    print('-'*60)
    s(0.8)
  print('_'*60)
  print('_'*60)
Search()