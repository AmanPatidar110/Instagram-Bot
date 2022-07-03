from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import random
from selenium.common.exceptions import NoSuchElementException

#/html/body/div[5]/div/div[2]/div/div/div[1]/div[2]/div[1]/div



usrname = "swipe_facts"
pwd = "Airc00ler@"
tag = ['factsinhindi','chankyaquotes','chankya','hindifacts','hindimotivationalquotes','hindifactopedia','hindifacctstation','hindifactsindia','currentaffairs','currentaffairshindi','hindigk','upsc','hindisuvichar']

target = ['hindi.suvichar','hindifacts4u','hindifact','gk__india____','gk_of_bharat','gk_questions_daily']

class MahBot() :

    def __init__(self,usrname,pwd) :
        self.bot= webdriver.Chrome()
        self.usrname = usrname
        self.pwd = pwd
        self.bot.get("https://www.instagram.com/")
        time.sleep(random.randint(3,5))

        
    def login(self) :
        self.bot.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(self.usrname)

        self.bot.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(self.pwd)
       
        self.bot.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]').click()

        time.sleep(random.randint(3,5))

        self.bot.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button').click()

        time.sleep(random.randint(3,5))

        self.bot.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()

        time.sleep(random.randint(3,5))
    


    def Hashtags(self,tag) :

        random.shuffle(tag)
        
        self.bot.get('https://www.instagram.com/explore/tags/{}'.format(tag[0]))
        Tolike = random.randint(5,8)
        Likes = self.Likefunc(Tolike)

        return Likes


    def Open(self,target) :
        scroll = 0
        count = 1
        Follow = 0
        random.shuffle(target)

        rand = random.randint(3,5)
        while Follow <=  rand:
            time.sleep(2)
            
            try:
                #self.bot.get('https://www.instagram.com/{}'.format(target[0]))
                self.bot.get('https://www.instagram.com/gk_questions_daily/')

            except TypeError:
                continue

            time.sleep(random.randint(2,5))
            self.bot.find_elements_by_class_name('_9AhH0')[0].click()
            time.sleep(random.randint(3,5))


            try:
                self.bot.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.EDfFK.ygqzn > div > div.Nm9Fw > button').click()
            
            except NoSuchElementException:
                continue

            time.sleep(random.randint(3,5))




            if count >= 7 :
                try:
                    target = self.bot.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div/div[7]/div[2]/div[1]/div')
                    scroll +=1

                    self.bot.execute_script('arguments[0].scrollIntoView(true);', target)
                    time.sleep(2)

                    if count == 11:
                        count = 7
                        target = self.bot.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div/div[11]/div[2]/div[1]/div')
                        self.bot.execute_script('arguments[0].scrollIntoView(true);', target)
                        scroll +=1
                    
                    if scroll >= 2 and count >= 11:
                        count = 7
                        target = self.bot.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div/div[11]/div[2]/div[1]/div')
                        self.bot.execute_script('arguments[0].scrollIntoView(true);', target)
                        scroll +=1


                        
                except NoSuchElementException:
                    break


            
            box = ''
                
            try :
                while box != 'Follow':

                    try :
                        box = self.bot.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div/div[{}]/div[3]/button'.format(count)).text
                    

                    except NoSuchElementException:
                        continue

                    finally :
                        if box != 'Follow' :
                            count += 1

            except NoSuchElementException:
                continue


            
            time.sleep(random.randint(2,4))
            try :
                self.bot.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div/div[{}]/div[2]/div[1]/div'.format(count)).click()
                time.sleep(random.randint(2,3))
   
            except NoSuchElementException:
                continue

            count += 1

            try:
                Follow += self.Follow_Like()
                continue

            except TypeError:
                Follow = 0
                continue

            except NoSuchElementException :
                continue

            except RuntimeError:
                continue
            
            except IndexError:
                continue

            except :
                continue

        return Follow



    def Follow_Like(self) :
        Follow = 0
        Button = None
        time.sleep(random.randint(2,5))
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
                Button = self.bot.find_element_by_css_selector('#react-root > section > main > div > header > section > div.nZSzR > button')
                        

            except NoSuchElementException:
                pass

                

        Followers = self.bot.find_elements_by_class_name('g47SY')[1].text

        Followers = ''.join([i for i in Followers if i.isdigit()])
            
            
        Following = self.bot.find_elements_by_class_name('g47SY')[2].text
        Following = ''.join([i for i in Following if i.isdigit()])


        if  Button.text == 'Follow'  :

            if int(Followers) <= int(Following):
                Button.click()
                Follow += 1
                time.sleep(2)
                    
                try :
                    if Button == self.bot.find_element_by_css_selector('#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_._4EzTm > span > span.vBF20._1OSdk > button') or Button ==  self.bot.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/div/span/span[1]/button') :
                        try:
                            target = self.bot.find_elements_by_class_name('_9AhH0')[0]

                            self.bot.execute_script('arguments[0].scrollIntoView(true);', target)
                            time.sleep(2)



                        except IndexError :
                            return RuntimeError

                        try:
                            Likes = self.Likefunc(3)
                            print(Likes)
                            return Follow
                            
                                
                        except NoSuchElementException :
                            return NoSuchElementException


                    else :
                        return Follow

                except NoSuchElementException:
                    return NoSuchElementException


            else :
                return Follow
                

        else:
            return Follow


        return Follow           



    def Likefunc(self,Tolike) :
        time.sleep(random.randint(3,4))
        self.bot.find_elements_by_class_name('_9AhH0')[0].click()
        time.sleep(random.randint(3,4))

        Likes=0
        
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


            time.sleep(random.randint(2,5))
            try :
                self.bot.find_element_by_class_name('_65Bje').click()

            except NoSuchElementException:
                return NoSuchElementException
                
            time.sleep(random.randint(2,5))  

        return Likes  



    def closeBrowser(self) :
        self.bot.close()
    



def main():
    igbot = MahBot(usrname,pwd)
    igbot.login()

    Following = 0
    Likes = 0

    start = time.time()

    while Following <= 10 :
        Following += igbot.Open(target)
        #Likes += igbot.Hashtags(tag)

    print('Followed Till Now! : ' + Following)
    print('Liked From Hashtags: '+Likes)

    #igbot.test()
    igbot.closeBrowser()

    print(start - time.time())


if __name__ == "__main__":
    main()
    



