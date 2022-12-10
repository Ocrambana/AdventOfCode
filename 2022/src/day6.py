
def markerRecognition(s,n):
    last = ""
    index = -1
    for i in range(len(s)):
        chr = s[i]
        if chr not in last:
            last = last + chr
        else:
            pos = last.find(chr)
            last = last[pos+1:] + chr
        
        if len(last) == n:
            return i+1


if __name__ == "__main__":
    print("day6")
    length = 14
    # test = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    # print(str(markerRecognition(test, length)))
    # print(str(markerRecognition("bvwbjplbgvbhsrlpgdmjqwftvncz", length)))
    # print(str(markerRecognition("nppdvjthqldpwncqszvftbrmjlhg", length)))
    # print(str(markerRecognition("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", length)))
    # print(str(markerRecognition("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", length)))
    with open("../data/6-input.txt","r") as data:
        for line in data:
            print(str(markerRecognition(line, length)))
