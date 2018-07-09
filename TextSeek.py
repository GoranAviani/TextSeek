import os
import collections

SearchResult = collections.namedtuple("SearchResult", "file, line, text")

def main():
    print_header()
    folderPath = get_folder_from_user()


    if not folderPath:
        print("Sorry, that location can't be found.")
        return

    text = get_search_text_from_user()
    if not text:
        print("Can't search for nothing, please input some text which will be searched.")

    matches = search_folders(folderPath, text)

    #print results
    print_results(matches)

    #for match in matches:
    #    print(match)

def print_results(matches):
    for match in matches:
        print("----------MATCH-----------")
        print("file {}".format(match.file))
        print("line: {} ".format(match.line))
        print("match text: {}".format(match.text.strip()))


def print_header():
    print("-----------------------------------------------------")
    print("                  TextSeek                           ")
    print("-----------------------------------------------------")

#Folder where it will be searched
def get_folder_from_user():
    folder = input("What folder do you want to search for: ")
    #folder is empty, none or if it is just whitespace return None
    if not folder or not folder.strip():
        return None

    #if it is not a directory return None
    if not os.path.isdir(folder):
        return None

    #Return absolute path of folder
    folderPath = os.path.abspath(folder)
    return folderPath

#Word that will be searched for
def get_search_text_from_user():
    text = input("What do you want to search for, single phrases only: ")
    return text.lower()



def search_folders(folderPath, text):

    allMatches=[]

    #listdir gives only filenames in this folder, not full path name
    filesInFolder = os.listdir(folderPath)


    for file in filesInFolder:
        #adding path + name of folder as full path as listdir cant give more than just filename, no full path
        fullFilePath = os.path.join(folderPath, file)
        #print(folderPath)
        #print(file)
        #print(fullFilePath)

        #if its a folder skip it
        if os.path.isdir(file):
            continue

        #if its a file search it
        matches = search_file(fullFilePath, text)
        allMatches.extend(matches)

    return allMatches



def search_file(fullFilePath, searchText):
    matches = []
    with open(fullFilePath, "r", encoding = "utf-8") as fin:

        lineNumber = 0
        for line in fin:
            lineNumber = 0
            #if find is > 0 append the line to matches
            if line.lower().find(searchText) >= 0:
                m = SearchResult(line = lineNumber, file = fullFilePath, text = line)
                matches.append(m)

    return matches



if __name__ == "__main__":
    main()