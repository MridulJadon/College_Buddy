from selenium import webdriver
from time import sleep
from tkinter import *

def search():
    thing = enterNearbyField.get()
    place = enterPlaceField.get()
    driver = webdriver.Chrome("C:/Users/Dikshant Gupta/Documents/chromedriver")
    driver.get("https://www.google.com/maps")
    sleep(2)
    searchplace(thing,place,driver)
    directions(driver)

def searchplace(thing,place,driver):
    Place = driver.find_element_by_class_name("tactile-searchbox-input")
    Place.send_keys(f"{thing} near {place}")
    Submit = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
    Submit.click()

def directions(driver):
    sleep(10)
    direction = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/button/span")
    direction.click()

if __name__ == '__main__':
    gui = Tk()
    gui.configure(background="#292826")
    gui.title("To-Do List")
    gui.geometry("1000x600")

    font1 = "-family {Open Sans bold} -size 15"
    font2 = "-family {Open Sans bold} -size 10"
    font3 = "-family {Open Sans Semibold} -size 10"

    enterNearby = Label(gui, text="Search for...", font=font1, bg="#f9d342", fg="#292826")
    enterNearbyField = Entry(gui, bg="#fffbf2")
    enterPlace = Label(gui, text="Enter a place", font=font1, bg="#f9d342", fg="#292826")
    enterPlaceField = Entry(gui, bg="#fffbf2")

    Search = Button(gui, text="Search", font=font2, fg="#f9d342", bg="#292826",command=search)

    enterNearby.pack(fill='x')
    enterNearbyField.pack(fill='x', pady=10, padx=400)
    enterPlace.pack(fill='x', pady=10)
    enterPlaceField.pack(fill='x', padx=400)
    Search.pack(fill='x', padx=450, pady=30)

    gui.mainloop()