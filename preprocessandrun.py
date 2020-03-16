import scrape
import read
import run

def main():
    scrape.scrape("Pennsylvania")
    print("Scrape finished")
    run.train("config.json")
    read.read()
main()
