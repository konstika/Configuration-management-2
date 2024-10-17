import os
import sys
import subprocess

if(len(sys.argv)<3):
    p = subprocess.Popen(["start", "cmd", "/k", 'cd /Users/aser/kisscm/ && git log --pretty=format:"%H:%P" --since=2.years > commits.txt'], shell = True)
else:
    p = subprocess.Popen(["start","cmd", "/k", 'cd '+sys.argv[1]+' && git log --pretty=format:"%H:%P" --since='+sys.argv[2]+' > commits.txt'], shell = True)
with open("/Users/aser/kisscm/commits.txt") as file:
    commits=[]
    parents=[]
    plantUML = "@startuml\n"
    for line in file:
        line=(line.replace('"',"")).replace('\n',"")
        commits.append(line.split(':')[0])
        parents.append((line.split(':')[1]).split(' '))

        
    for i in range(len(commits)):
        for parent in parents[i]:
            if parent=="" or not(parent in commits):
                plantUML+="("+commits[i]+")\n"
            else:
                plantUML+="("+parent+") --> ("+commits[i]+")\n"

    plantUML+="@enduml"
    graph = open("graph_commits.puml","w")
    graph.write(plantUML)
    graph.close()
    file.close()
    p = subprocess.Popen(["start", "cmd", "/k",
                          'cd '+sys.argv[0].replace(sys.argv[0].split('/')[-1],"")+' && python -m plantuml graph_commits.puml && graph_commits.png'],shell = True)
