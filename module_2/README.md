# DevOPS Pamati
## Tēma 2
>1\. Iepazīsties ar komandas git log opcijām pēc
[https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)
*
    ```sh
    $ git log
    $ git log -p -2
    $ git log --pretty=oneline
    $ git log --stat
    $ git log --pretty=format:"%h - %an, %ar : %s"
    $ git log --since=2.weeks
    $ git log -S function_name
    $ git log -- path/to/file
    $ git log --pretty="%h - %s" --author='Junio C Hamano' --since="2008-10-01" --before="2008-11-01" --no-merges -- t/
    ```

>2\. Izveidot Jūsu darba stacijā ssh atslēgas un iekopēt publisko atslēgu GitHub.
*
    ```sh
    ssh-keygen -b 4096 -t ed25519 -f ./id_devops_pamati
    ```

>3\. Noklonēt no GitHub vietnes pirmajā mājas darbā izveidoto repozitoriju lokālajā darba stacijā. 
>Repozitorijam, kuru izmantosiet kursa laikā, atvelēt atsevišķu mapi ar nosaukumu git_repos
*
    ```sh
    mkdir git_repos
    cd ./git_repos
    git clone git@github.com:evldog/devops_basic_eduardsklesc.git
    ```

>4\. Lokālajā repozitorijā izveidot mapes module_1 un module_2
*
    ```sh
    mkdir ./module_1
    mkdir ./module_2
    ```

>5\.Iepazīsties ar Mark Down valodas elementiem - https://dillinger.io/
* Ok

>6\. Mapē module_1 izveidot README.md failu.
*
    ```sh
    cd ./module_1
    copy CON README.md
    notepad README.md
    ```

>7\. Stilistiski, pēc Jūsu uzskata, noformēt README.md failu tā, lai tas saturētu pirmā mājas darba uzdevuma >saturu. Informācija par autoru (varat likt tikai vārdu), links uz github projektu un attēls (ja tas ir >iespējams). Bildes un papildus materiālus obligāti ievietot repozitorijā.
*
    ```sh
    cd ./module_1
    copy CON README.md
    notepad README.md
    ```

>8\. Ar git palīdzību noformēt commit un pārsūtīt rezultātu github.
*
    ```sh
    cd ..
    git add -A
    git commit -m "Tema 2. Uzdēvums 8"
    ```

>9\. Pārbaudīt kāds commit hash ir lokālajā git repozitorijā un salīdzināt to ar šī paša faila commit hash github.
*
    ```sh
    git log
    ```
    | commit id locally | commit id on github.com |
    | ------ | ------ |
    | 2f710078904ac5e3d713169faf194f45027e2a03 | 2f710078904ac5e3d713169faf194f45027e2a03 |
    Git commit hash is the same 

>10\. Mapē module_2 izveidot README.md failu.
*
    ```sh
    cd ./module_2
    copy CON README.md
    ```
>11\. Iekopēt trūkstošos failus (bildes vai citus) no module_1 mapē module_2. README.md failu neaiztikt.
*
    ```sh
    copy ../module_1/*.py ./
    copy ../module_1/*.png ./
    ```

>12\. Ar git palīdzību noformēt commit un pārsūtīt rezultātu github.
*
    ```sh
    cd ..
    git add -A
    git commit -m "Tema 2. Uzdēvums 12"
    ```

>13\. Salīdzināt vienādu failu (ne README) hash no mapes module_1 un module_2. Vai git redz atšķirību starp šiem failiem?
*
    ```sh
    $ git cat-file -p main^{tree}:module_1 | grep hello_world.py | awk '{print $3}'
    $ git cat-file -p main^{tree}:module_2 | grep hello_world.py | awk '{print $3}'
    ```
    | module_1/hello_world.py | module_2/hello_world.py |
    | ------ | ------ |
    | 5e91ef2e6d05adaa9e8860202fb5acc511a82589 | 5e91ef2e6d05adaa9e8860202fb5acc511a82589 |
    
    Git sees files with the same content size as one entity with the same id (hash)
	So we can conclude that de-duplication mechanism is in place

>14\. Rezultātus apkopot module_2 README.md
*
    Done
    

>15\. Mapē git_repos noklonēt https://github.com/hashicorp/terraform projektu.
*
    ```sh
    $ git clone https://github.com/hashicorp/terraform
    ```

>16\. Pārbaudīt kādas izmaiņas tika veiktas iepriekšējās nedēļas laikā. Atrast vismaz divus veidus kā to izdarīt.
*
    ```sh
    $ git log --since=1.week
    $ git log --pretty=format:"%h - %an, %ar"
    ```

>17\. Atrast commit kurus veica autors - “Laura Pacilio”
*
    ```sh
    $ git log --author='Laura Pacilio' --pretty=oneline
    ```
    Laura was very productive and made a lot of commits
    

>18\. Atrast vai Laura ir veikusi commit pagājušā gada septembrī?
*
    ```sh
    $ git log --author='Laura Pacilio' --pretty=oneline --since="2021-09-01" --before="2021-10-01"
    ```
    Yes, Laura has performed a commit in Spetember 2021

>19\. Vai Laura ir veikusi commit vakar?
*
    ```sh
    $ git log --author='Laura Pacilio' --pretty=oneline --since="1 day"
    ```
    No, Laura has not performed a commit yesterday

>20\. Rezultātus apkopot module_2\>README.md un pārsūtīt rezultātu github.
*
    Done

>21\*\. Atlasot rezultātus no pagājušā gada 20 līdz 21 aprīlim var atrast commit kurš ir datēts ar 16 aprīli? Kāpēc tā ir? Atbildi apkopot module_2 >README.md un pārsūtīt rezultātu Github.
*
    ```sh
    $ git log --pretty=format:"%h - %cd, %ad, %cr, %an, %ar" --since="2021-20-04" --before="2021-21-04"
    ```
    Because author date and commit date are two different things.
    Change was made on Friday, and hasn't been commited. We can imagine, that author forgot to commit it.
    
    | commit id  | Committer date | Author date | Committer date, relative | Author name | 	Author date, relative | 
    | ------ | ------ | ------ | ------ | ------ | ------ |
    | f8493bf5c |  Tue Apr 20 17:04:56 2021 -0400 |  Fri Apr 16 17:11:27 2021 -0400 |  1 year ago | James Bardin |  1 year ago
    | d15f7394a |  Tue Apr 20 16:25:34 2021 -0400 |  Tue Apr 20 16:25:34 2021 -0400 |  1 year ago |  James Bardin |  1 year ago
    | 7f571b5eb |  Tue Apr 20 12:31:32 2021 -0400 |  Tue Apr 20 12:31:32 2021 -0400 |  1 year ago |  James Bardin |  1 year ago


## Autors
_Eduards_
