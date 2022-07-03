from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd


#/html/body/div[5]/div/div[2]/div/div/div[1]/div[2]/div[1]/div



# "swipe_facts",
# "Airc00ler@",

# ['factsinhindi','chankyaquotes','chankya','hindifacts','hindimotivationalquotes','hindifactopedia','hindifactstation','hindifactsindia','currentaffairs','currentaffairshindi','hindigk','upsc','hindi','hindiquotes','hindisayri','hindiwritersofinstagram','hindiwriting','hindiwriter','hindisuvichar'],

# ['hindi.suvichar','hindifacts4u','hindifact','gk__india____','gk_of_bharat','hindiquotes','hindi_panktiyaan','hindihealth','hindisuvichar','hindiwriters','hindiwikipedia','sandeep_maheshwari_hindi','hindi_writer','hindi.quote','makeinindia','hindi_gk_','scienceinhindi'],

#usrnames = ["amanpatidar110@gmail.com","urban_libaaz"]
#pwd = ["Aamanpati110!","Airc00ler!"]
#tag = (['fashion','fashionstyle','fashionblogger','fashioninsta','fashionnova','fashiongram','fashionblog','fashiongoals','fashionindia','fashioninindia','indorefashion','delhifashion','mumbaifashion','punjabfashion','fashionforall','desifashion','desifashioninsta','fashiondesign','vocalforlocal','madeinindia','vocalforlocalindia'],['fashion','fashionstyle','fashionblogger','fashioninsta','fashionnova','fashiongram','fashionblog','fashiongoals','fashionindia','fashioninindia','indorefashion','delhifashion','mumbaifashion','punjabfashion','fashionforall','desifashion','desifashioninsta','fashiondesign','vocalforlocal','madeinindia','vocalforlocalindia'])

#target = (['hindi.suvichar','hindifacts4u','hindifact','gk__india____','gk_of_bharat','hindiquotes','hindi_panktiyaan','hindihealth','hindisuvichar','hindiwriters','hindiwikipedia','sandeep_maheshwari_hindi','hindi_writer','hindi.quote','makeinindia','hindi_gk_','scienceinhindi'],['themrsingh','styleonair_','stylebyinder','riwaayatt','cloakedkitten','lifestyleofindia','lifestylebydebashri','jatt.life.style','doctorelvishvixen','dhiman_ajay_','muskan_yadv','ktm_duke_shootout','forevernew_india','the_new_india_','shopnew__india','makeinindia','indorefashionexplorer_','teachingthem'])

class MahBot() :

    def __init__(self,usrname,pwd,follow_visited,like_visited,target) :
        self.bot= webdriver.Chrome()
        self.usrname = usrname
        self.pwd = pwd
        self.target = target
        self.follow_visited = follow_visited
        self.like_visited = like_visited
        self.bot.get("https://www.instagram.com/")
        time.sleep(random.randint(3,5))


        
    def login(self) :
        self.bot.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(self.usrname)

        self.bot.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(self.pwd)
       
        self.bot.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]').click()

        time.sleep(random.randint(3,4))

        NotNow = WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#react-root > section > main > div > div > div > div > button")))
        NotNow.click()

        time.sleep(random.randint(2,4))

        self.bot.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

        time.sleep(random.randint(2,4))
    


    def Hashtags(self,tag,lih) :

        random.shuffle(tag)
        try:
            self.bot.get('https://www.instagram.com/explore/tags/{}'.format(tag[0]))

        except IndexError:
            random.shuffle(tag)
            self.bot.get('https://www.instagram.com/explore/tags/{}'.format(tag[0]))
            

        Tolike = random.randint(lih[0],lih[1])
        Likes = self.Likefunc(Tolike)

        return Likes






    def Open(self,id_list) :
        append = 0
        count = 1
        random.shuffle(self.target)
 
        try:
            self.bot.get('https://www.instagram.com/{}'.format(self.target[0]))
            

        except TypeError:
            return id_list


        Followers = self.bot.find_elements_by_class_name('g47SY')[1].text
        Followers = ''.join([i for i in Followers if i.isdigit()])
            
        Following = self.bot.find_elements_by_class_name('g47SY')[2].text
        Following = ''.join([i for i in Following if i.isdigit()])

        if int(Followers) >= int(Following):
            time.sleep(random.randint(2,5))
            try:
                self.bot.find_elements_by_class_name('_9AhH0')[0].click()
                time.sleep(random.randint(3,5))

            except IndexError:
                return id_list



            try:
                self.bot.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.EDfFK.ygqzn > div > div.Nm9Fw > button').click()
            
            except NoSuchElementException:
                return id_list
        
            except :
                return id_list


            time.sleep(random.randint(2,3))


            while append <= 35:
               if count == 7 or count>=11 :
                   try:

                       scrl = self.bot.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/div/div[7]/div[2]/div[1]/div')
                    
                       self.bot.execute_script('arguments[0].scrollIntoView(true);', scrl)
                       time.sleep(1)

                       count = 7
                                        
                   except NoSuchElementException:
                       break

               box = ''
                
               try :
                   while box != 'Follow':
                       try :
                           box = self.bot.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/div/div[{}]/div[3]/button'.format(count)).text
                  

                       except NoSuchElementException:
                           break

                       finally :
                           if box != 'Follow' :
                               count += 1
                               

                   if count == 7 or count>=11 :

                       try:
                           scrl = self.bot.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/div/div[7]/div[2]/div[1]/div')
                           self.bot.execute_script('arguments[0].scrollIntoView(true);', scrl)
                           time.sleep(1)

                           count = 7
                           
                                        
                       except NoSuchElementException:
                           return id_list
                                
                       except: 
                           return id_list

               except NoSuchElementException:
                   break


               try :
                   u = self.bot.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/div/div[{}]/div[2]/div[1]/div/a'.format(count)).get_attribute('title')
                   if (u not in id_list) and (u not in self.follow_visited) :
                       id_list.append(u)
                       append += 1
                       count += 1
                       

                   else :
                       count += 1
                       continue
                    
                    

               except NoSuchElementException:
                       count += 1
                       continue
               except:
                   break

        return id_list



        


    def Followfunc(self,id_list,fior) :
        Follow = 0
             
        rand = random.randint(fior[0],fior[1])
        while Follow <= rand:
            time.sleep(random.randint(2,3))
            
            if len(id_list) <= 10:
                self.Open(id_list)
            
            try :
                if id_list[0] in self.follow_visited:
                    id_list.pop(0)
                    continue
            
            except:
                pass


            try:
                self.bot.get('https://www.instagram.com/{}/'.format(id_list[0]))
                self.follow_visited.append(id_list[0])

            except TimeoutException:
                continue

            except :
                continue

            time.sleep(random.randint(3,4))
            
            WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button")))

            
            Followers = self.bot.find_elements_by_class_name('g47SY')[1].text
            Followers = ''.join([i for i in Followers if i.isdigit()])
            
            Following = self.bot.find_elements_by_class_name('g47SY')[2].text
            Following = ''.join([i for i in Following if i.isdigit()])

            if int(Followers) <= int(Following):

                try :
                    CLICK = self.GetButton()

                except StaleElementReferenceException:
                    self.bot.refresh
                    CLICK = self.GetButton()
                
                except NoSuchElementException:
                    continue

                if  CLICK.text == 'Follow'  :
                    CLICK.click()
                    Follow += 1
                    id_list.pop(0)
                    time.sleep(random.randint(1,2))


                else :
                    id_list.pop(0)
                    continue
                            
            else:
                id_list.pop(0)
                continue 
       
        return Follow, id_list          



    def Likefunc(self,Tolike) :

        try:
            scrl = self.bot.find_elements_by_class_name('_9AhH0')[0]

            self.bot.execute_script('arguments[0].scrollIntoView(true);', scrl)
            



        except IndexError :
            return NoSuchElementException
        except :
            return NoSuchElementException

        time.sleep(random.randint(2,3))
        Likes=0

        try:
            self.bot.find_elements_by_class_name('_9AhH0')[0].click()

        except IndexError:
            return Likes
            
        time.sleep(random.randint(2,3))

        
        while Likes < Tolike:
            try:
                heart = self.bot.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > svg')
        
                if heart.get_attribute("aria-label") == "Like" :
                    heart.click()
                    Likes += 1
            
                else :
                    pass


            except NoSuchElementException:
                pass

            time.sleep(random.randint(2,3))
            try :
                self.bot.find_element_by_class_name('_65Bje').click()

            except NoSuchElementException:
                return NoSuchElementException
                
            time.sleep(random.randint(2,3))  

        return Likes  




    def GetButton(self) :
        Button = None

        try:
            Button = self.bot.find_element_by_css_selector('#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_._4EzTm > span > span.vBF20._1OSdk > button')
                
        except NoSuchElementException:
            pass
            
        if Button == None :
            try :
                Button = self.bot.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/button')
                        
            except NoSuchElementException:
                pass
                

                
        if Button == None :
            try :
                Button = self.bot.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/div/span/span[1]/button')
                        
            except NoSuchElementException :
                pass
              
           
        if Button == None :
            try :
                Button = self.bot.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/button')
                        
            except NoSuchElementException :
                pass
                

        if Button == None :
            try :
                Button = self.bot.find_element_by_css_selector('button')
                        
            except NoSuchElementException :
                pass

        if Button == None :
            return NoSuchElementException

        return Button


    def GetFollowers(self) :
        append = 0
        count = 1
        time.sleep(2)
        try:
            self.bot.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a').click()
            

        except:
            return self.target

        time.sleep(random.randint(3,5))


        try:
            fo = WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#react-root > section > main > div > header > section > ul > li:nth-child(2) > a")))
            fo.click()
            

        except IndexError:
            return self.target




        time.sleep(random.randint(2,3))



        while append <= 20:
           

            try :
                u = self.bot.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[{}]/div/div[1]/div[2]/div[1]/a'.format(count))
                
                uid = u.get_attribute('title')
                if (uid not in self.target) and (uid not in self.like_visited) :
                    self.target.append(uid)
                    append += 1
                    count += 1
                    time.sleep(1)

                else :
                    count += 1
                    continue
                    
                    
            except NoSuchElementException:
                count += 1
                break
            except:
                break

        return self.target





    def Following(self,following_list) :
        append = 0
        count = 1
        time.sleep(2)
        try:
            self.bot.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img').click()
            
        except:
            return following_list

        time.sleep(random.randint(3,5))


        try:
            fo = WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")))

            fo.click()
            

        except IndexError:
            return following_list



        time.sleep(random.randint(2,3))



        while append <= 20:
            
            try :
                u = self.bot.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child({}) > div > div.t2ksc > div.enpQJ > div.d7ByH > a'.format(count))
                
                uid = u.get_attribute('title')

                if (uid not in following_list) and (uid not in self.like_visited) :
                    following_list.append(uid)
                    append += 1
                    count += 1
                    time.sleep(1)

                else :
                    count += 1
                    continue
                    
                    
            except NoSuchElementException:
                count += 1
                continue
            except:
                break

        return following_list




    def Like_following(self,following_list,lip,vtl) :
        visit = 0
        if len(following_list) < 25:
            self.Following(following_list)
         
        rand = random.randint(vtl[0],vtl[1])
        while visit <= rand:

            if len(following_list) < 10:
                self.Following(following_list)
            
            time.sleep(random.randint(2,3))
            try :
                if following_list[0] in self.like_visited:
                    following_list.pop(0)
                    continue
            
            except:
                pass


            try:
                self.bot.get('https://www.instagram.com/{}/'.format(following_list[0]))
                self.like_visited.append(following_list[0])
                

            except TimeoutException:
                self.bot.refresh()

            except :
                continue

            time.sleep(random.randint(2,3))
            if len(following_list) <= 10:
                self.Following(following_list)

            try:
                self.Likefunc(random.randint(lip[0],lip[1]))
                visit += 1
                following_list.pop(0)
                continue           
                                    
            except NoSuchElementException :
                following_list.pop(0)
                continue

        return following_list

            



    def closeBrowser(self) :
        self.bot.close()





def main():
    id_number = 0
    
    id_list = []
    following_list = []
    sheet = pd.read_excel('Untitled spreadsheet.xlsx')

    while id_number < len(sheet['usernames']):
        
        tag = sheet['tags'][id_number].split()
        usrnames = sheet['usernames'][id_number]
        pwd = sheet['passwords'][id_number]
        target = sheet['target'][id_number].split()
        follow_visited= sheet['visited to follow'][id_number].split()
        like_visited = sheet['visited to like'][id_number].split()
        Follow_in_one_round = sheet['follow in one round'][id_number].split()
        Like_in_hashtag = sheet['like in hashtag in one round'][id_number].split()
        Like_in_profile = sheet['like in every profile'][id_number].split()
        Visits_to_like_in_1_round = sheet['visits to like in one round'][id_number].split()
        Total_follow = int(sheet['total follow'][id_number])


        fior= [int(e) for e in Follow_in_one_round]
        lih= [int(e) for e in Like_in_hashtag]
        lip= [int(e) for e in Like_in_profile]
        vtl= [int(e) for e in Visits_to_like_in_1_round]


        igbot = MahBot(usrnames,pwd,follow_visited,like_visited,target)
        igbot.login()
        
        Following = 0
        Likes = 0

        start = time.time()

        while Following <= Total_follow :
            follow_visited= sheet['visited to follow'][id_number].split()
            like_visited = sheet['visited to like'][id_number].split()

            igbot.GetFollowers()
            id_list += igbot.Open(id_list)
            Likes += igbot.Hashtags(tag,lih)
            Follow, id_list = igbot.Followfunc(id_list,fior)
            Following += Follow
            following_list = igbot.Following(following_list)
            following_list = igbot.Like_following(following_list,lip,vtl)



            

            put_target = ' '.join([str(elem) for elem in igbot.target])
            put_follow_visited = ' '.join([str(elem) for elem in igbot.follow_visited])
            put_like_visited = ' '.join([str(elem) for elem in igbot.like_visited])

            

            sheet['target'][id_number] = put_target
            sheet['visited to follow'][id_number] = put_follow_visited 
            sheet['visited to like'][id_number] = put_like_visited

            sheet.to_excel('Untitled spreadsheet.xlsx', index = False)

        print('Followed Till Now! : {}'.format(Following))
        print('Likes in Hashtags : {}'.format(Likes))

        
        igbot.closeBrowser()
        print(time.time() - start)
        


        id_number += 1


if __name__ == "__main__":
    main()
    



