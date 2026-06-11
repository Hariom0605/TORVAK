import json

commands = {}

# ══════════════════════════════════════════════════════════════
# CATEGORY 1: BROWSERS
# ══════════════════════════════════════════════════════════════
commands["open_chrome"] = ["open chrome","launch chrome","start chrome","run chrome","chrome","go to chrome","fire up chrome","open google chrome","launch google chrome","start google chrome","run google chrome","google chrome"]
commands["open_firefox"] = ["open firefox","launch firefox","start firefox","run firefox","firefox","go to firefox","fire up firefox","open mozilla","launch mozilla","start mozilla","mozilla firefox"]
commands["open_edge"] = ["open edge","launch edge","start edge","run edge","edge","open microsoft edge","launch microsoft edge","start microsoft edge","microsoft edge","open ms edge"]
commands["open_brave"] = ["open brave","launch brave","start brave","run brave","brave","brave browser","open brave browser","launch brave browser"]
commands["open_opera"] = ["open opera","launch opera","start opera","run opera","opera","opera browser","open opera browser"]
commands["open_vivaldi"] = ["open vivaldi","launch vivaldi","start vivaldi","vivaldi"]
commands["open_tor"] = ["open tor","launch tor","start tor","tor browser","open tor browser"]
commands["open_ie"] = ["open internet explorer","launch internet explorer","internet explorer","ie","open ie"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 2: CODE EDITORS & IDEs
# ══════════════════════════════════════════════════════════════
commands["open_vscode"] = ["open vscode","launch vscode","start vscode","run vscode","vscode","open vs code","launch vs code","start vs code","vs code","open visual studio code","launch visual studio code","visual studio code","code editor","open code","launch code"]
commands["open_pycharm"] = ["open pycharm","launch pycharm","start pycharm","run pycharm","pycharm","open pycharm ide","launch pycharm ide","pycharm ide"]
commands["open_intellij"] = ["open intellij","launch intellij","start intellij","intellij","open intellij idea","launch intellij idea","intellij idea"]
commands["open_sublime"] = ["open sublime","launch sublime","start sublime","sublime","sublime text","open sublime text","launch sublime text"]
commands["open_atom"] = ["open atom","launch atom","start atom","atom","atom editor","open atom editor"]
commands["open_notepadpp"] = ["open notepad++","launch notepad++","notepad++","npp","open npp","launch npp","open notepad plus plus"]
commands["open_vim"] = ["open vim","launch vim","vim","start vim"]
commands["open_android_studio"] = ["open android studio","launch android studio","android studio","start android studio"]
commands["open_eclipse"] = ["open eclipse","launch eclipse","eclipse","start eclipse"]
commands["open_netbeans"] = ["open netbeans","launch netbeans","netbeans"]
commands["open_visual_studio"] = ["open visual studio","launch visual studio","visual studio","vs","open vs","launch vs","microsoft visual studio"]
commands["open_jupyter"] = ["open jupyter","launch jupyter","jupyter","jupyter notebook","open jupyter notebook","launch jupyter notebook","start jupyter"]
commands["open_spyder"] = ["open spyder","launch spyder","spyder","spyder ide"]
commands["open_cursor"] = ["open cursor","launch cursor","cursor","cursor editor","cursor ai","open cursor ai"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 3: SYSTEM APPS — WINDOWS
# ══════════════════════════════════════════════════════════════
commands["open_notepad"] = ["open notepad","launch notepad","start notepad","notepad","open text editor","launch text editor","text editor"]
commands["open_calculator"] = ["open calculator","launch calculator","start calculator","calculator","calc","open calc","launch calc"]
commands["open_paint"] = ["open paint","launch paint","start paint","paint","ms paint","open ms paint","microsoft paint"]
commands["open_paint3d"] = ["open paint 3d","launch paint 3d","paint 3d","paint3d"]
commands["open_wordpad"] = ["open wordpad","launch wordpad","wordpad","start wordpad"]
commands["open_snipping_tool"] = ["open snipping tool","launch snipping tool","snipping tool","snip","snipper","screen snip","open snip"]
commands["open_sticky_notes"] = ["open sticky notes","launch sticky notes","sticky notes","stickies","open stickies"]
commands["open_clock"] = ["open clock","launch clock","clock app","alarm clock","open alarm","open timer","open stopwatch"]
commands["open_calendar"] = ["open calendar","launch calendar","calendar","show calendar","open windows calendar"]
commands["open_weather"] = ["open weather","launch weather","weather app","show weather","check weather app"]
commands["open_maps"] = ["open maps","launch maps","windows maps","open windows maps"]
commands["open_camera"] = ["open camera","launch camera","camera","webcam","start camera","open webcam"]
commands["open_photos"] = ["open photos","launch photos","photos","photo viewer","open photo viewer","windows photos"]
commands["open_movies"] = ["open movies","launch movies","movies and tv","open movies and tv"]
commands["open_groove"] = ["open groove","launch groove","groove music","open groove music","music player"]
commands["open_media_player"] = ["open media player","launch media player","windows media player","wmp","open wmp"]
commands["open_voice_recorder"] = ["open voice recorder","launch voice recorder","voice recorder","record voice","audio recorder"]
commands["open_mail"] = ["open mail","launch mail","mail app","windows mail","open windows mail","email app"]
commands["open_xbox"] = ["open xbox","launch xbox","xbox","xbox app","xbox game bar"]
commands["open_store"] = ["open store","launch store","microsoft store","windows store","open microsoft store","open windows store"]
commands["open_onedrive"] = ["open onedrive","launch onedrive","onedrive","open one drive","one drive"]
commands["open_cortana"] = ["open cortana","launch cortana","cortana"]
commands["open_news"] = ["open news","launch news","news app","windows news","microsoft news"]
commands["open_mixed_reality"] = ["open mixed reality","launch mixed reality","mixed reality portal"]
commands["open_phone_link"] = ["open phone link","launch phone link","phone link","your phone","open your phone"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 4: OFFICE & PRODUCTIVITY
# ══════════════════════════════════════════════════════════════
commands["open_word"] = ["open word","launch word","start word","word","microsoft word","ms word","open ms word","open microsoft word","open doc","open document editor"]
commands["open_excel"] = ["open excel","launch excel","start excel","excel","microsoft excel","ms excel","open ms excel","open spreadsheet","open microsoft excel"]
commands["open_powerpoint"] = ["open powerpoint","launch powerpoint","start powerpoint","powerpoint","ppt","ms powerpoint","microsoft powerpoint","open ppt","open presentation","open slides"]
commands["open_outlook"] = ["open outlook","launch outlook","outlook","microsoft outlook","ms outlook","open email client","outlook mail"]
commands["open_onenote"] = ["open onenote","launch onenote","onenote","one note","microsoft onenote","open one note"]
commands["open_teams"] = ["open teams","launch teams","teams","microsoft teams","ms teams","open ms teams","open team meeting"]
commands["open_access"] = ["open access","launch access","ms access","microsoft access","open database"]
commands["open_publisher"] = ["open publisher","launch publisher","ms publisher","microsoft publisher"]
commands["open_libreoffice"] = ["open libreoffice","launch libreoffice","libreoffice","libre office","open libre office"]
commands["open_libreoffice_writer"] = ["open libreoffice writer","libreoffice writer","libre writer","open writer"]
commands["open_libreoffice_calc"] = ["open libreoffice calc","libreoffice calc","libre calc","open libre calc"]
commands["open_libreoffice_impress"] = ["open libreoffice impress","libreoffice impress","libre impress","open libre impress"]
commands["open_notion"] = ["open notion","launch notion","notion","start notion"]
commands["open_obsidian"] = ["open obsidian","launch obsidian","obsidian","obsidian notes"]
commands["open_evernote"] = ["open evernote","launch evernote","evernote"]
commands["open_trello"] = ["open trello","launch trello","trello","open trello app"]
commands["open_slack"] = ["open slack","launch slack","slack","slack app","start slack"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 5: COMMUNICATION
# ══════════════════════════════════════════════════════════════
commands["open_whatsapp"] = ["open whatsapp","launch whatsapp","whatsapp","whats app","open whats app","start whatsapp"]
commands["open_telegram"] = ["open telegram","launch telegram","telegram","open telegram app"]
commands["open_discord"] = ["open discord","launch discord","discord","open discord app","start discord"]
commands["open_zoom"] = ["open zoom","launch zoom","zoom","zoom meeting","open zoom meeting","start zoom"]
commands["open_skype"] = ["open skype","launch skype","skype","microsoft skype","open skype app"]
commands["open_signal"] = ["open signal","launch signal","signal","signal app","signal messenger"]
commands["open_viber"] = ["open viber","launch viber","viber","viber app"]
commands["open_gmail"] = ["open gmail","launch gmail","gmail","go to gmail","open google mail"]
commands["open_yahoo_mail"] = ["open yahoo mail","yahoo mail","open yahoo","go to yahoo mail"]
commands["open_protonmail"] = ["open protonmail","protonmail","proton mail","open proton mail"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 6: MEDIA & ENTERTAINMENT
# ══════════════════════════════════════════════════════════════
commands["open_spotify"] = ["open spotify","launch spotify","spotify","open spotify app","start spotify","play spotify"]
commands["open_vlc"] = ["open vlc","launch vlc","vlc","vlc media player","open vlc player","open media player"]
commands["open_youtube"] = ["open youtube","launch youtube","youtube","go to youtube","open youtube website"]
commands["open_netflix"] = ["open netflix","launch netflix","netflix","go to netflix","open netflix website"]
commands["open_prime"] = ["open prime video","launch prime video","prime video","amazon prime","amazon prime video","open amazon prime"]
commands["open_hotstar"] = ["open hotstar","launch hotstar","hotstar","disney hotstar","open disney hotstar","open disney plus"]
commands["open_jiocinema"] = ["open jiocinema","jiocinema","jio cinema","open jio cinema"]
commands["open_zee5"] = ["open zee5","zee5","zee5","open zee 5"]
commands["open_sonyliv"] = ["open sonyliv","sonyliv","sony liv","open sony liv"]
commands["open_mxplayer"] = ["open mx player","mx player","mxplayer","launch mx player"]
commands["open_potplayer"] = ["open potplayer","potplayer","pot player","launch potplayer"]
commands["open_winamp"] = ["open winamp","winamp","launch winamp"]
commands["open_foobar"] = ["open foobar","foobar","foobar2000","launch foobar"]
commands["open_kodi"] = ["open kodi","kodi","launch kodi","kodi media center"]
commands["open_plex"] = ["open plex","plex","launch plex","plex media server"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 7: CREATIVE TOOLS
# ══════════════════════════════════════════════════════════════
commands["open_photoshop"] = ["open photoshop","launch photoshop","photoshop","adobe photoshop","ps","open ps","open adobe photoshop"]
commands["open_illustrator"] = ["open illustrator","launch illustrator","illustrator","adobe illustrator","ai","open adobe illustrator"]
commands["open_premiere"] = ["open premiere","launch premiere","premiere","adobe premiere","premiere pro","open premiere pro","open adobe premiere"]
commands["open_after_effects"] = ["open after effects","launch after effects","after effects","adobe after effects","ae","open ae"]
commands["open_audition"] = ["open audition","launch audition","audition","adobe audition","open adobe audition"]
commands["open_lightroom"] = ["open lightroom","launch lightroom","lightroom","adobe lightroom","open adobe lightroom"]
commands["open_acrobat"] = ["open acrobat","launch acrobat","acrobat","adobe acrobat","pdf editor","open pdf editor"]
commands["open_canva"] = ["open canva","launch canva","canva","go to canva","open canva website"]
commands["open_figma"] = ["open figma","launch figma","figma","go to figma","open figma app"]
commands["open_gimp"] = ["open gimp","launch gimp","gimp","open gimp editor","gnu image manipulation"]
commands["open_inkscape"] = ["open inkscape","launch inkscape","inkscape","open inkscape editor"]
commands["open_blender"] = ["open blender","launch blender","blender","3d blender","open 3d editor","blender 3d"]
commands["open_davinci"] = ["open davinci resolve","launch davinci resolve","davinci resolve","davinci","open davinci","resolve","video editor"]
commands["open_audacity"] = ["open audacity","launch audacity","audacity","audio editor","open audio editor"]
commands["open_obs"] = ["open obs","launch obs","obs","obs studio","open obs studio","streaming software","screen recorder"]
commands["open_kdenlive"] = ["open kdenlive","launch kdenlive","kdenlive","open video editor"]
commands["open_handbrake"] = ["open handbrake","launch handbrake","handbrake","video converter","open video converter"]
commands["open_capcut"] = ["open capcut","launch capcut","capcut","cap cut","open cap cut"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 8: DEVELOPMENT TOOLS
# ══════════════════════════════════════════════════════════════
commands["open_git"] = ["open git","launch git","git","git bash","open git bash","launch git bash"]
commands["open_github_desktop"] = ["open github desktop","launch github desktop","github desktop","github","open github app"]
commands["open_postman"] = ["open postman","launch postman","postman","api tester","open api tester"]
commands["open_insomnia"] = ["open insomnia","launch insomnia","insomnia","insomnia rest client"]
commands["open_docker"] = ["open docker","launch docker","docker","docker desktop","open docker desktop"]
commands["open_wsl"] = ["open wsl","launch wsl","wsl","windows subsystem for linux","open linux","open ubuntu"]
commands["open_terminal"] = ["open terminal","launch terminal","terminal","open command line","command line","open cli"]
commands["open_cmd"] = ["open cmd","launch cmd","cmd","command prompt","open command prompt","launch command prompt","dos prompt"]
commands["open_powershell"] = ["open powershell","launch powershell","powershell","ps","open ps","open windows powershell","launch powershell window"]
commands["open_wt"] = ["open windows terminal","launch windows terminal","windows terminal","wt","open wt"]
commands["open_putty"] = ["open putty","launch putty","putty","ssh client","open ssh client"]
commands["open_filezilla"] = ["open filezilla","launch filezilla","filezilla","ftp client","open ftp client"]
commands["open_wireshark"] = ["open wireshark","launch wireshark","wireshark","network analyzer","packet analyzer"]
commands["open_virtualbox"] = ["open virtualbox","launch virtualbox","virtualbox","virtual box","open virtual machine","vm"]
commands["open_vmware"] = ["open vmware","launch vmware","vmware","vmware workstation","open vmware workstation"]
commands["open_mongodb_compass"] = ["open mongodb compass","launch mongodb compass","mongodb compass","mongodb","open mongodb"]
commands["open_dbeaver"] = ["open dbeaver","launch dbeaver","dbeaver","db browser","database browser"]
commands["open_xampp"] = ["open xampp","launch xampp","xampp","open xampp control panel"]
commands["open_apache"] = ["open apache","launch apache","apache","apache server","start apache"]
commands["open_nginx"] = ["open nginx","launch nginx","nginx"]
commands["open_redis"] = ["open redis","launch redis","redis","redis server","open redis server"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 9: FILE MANAGER & FOLDERS
# ══════════════════════════════════════════════════════════════
commands["open_file_explorer"] = ["open file explorer","launch file explorer","file explorer","files","open files","open my computer","open this pc","this pc","my computer","open explorer","explorer","files manager","open file manager"]
commands["open_desktop"] = ["open desktop","show desktop","go to desktop","desktop folder","open desktop folder","navigate to desktop"]
commands["open_downloads"] = ["open downloads","go to downloads","downloads folder","open downloads folder","show downloads","navigate to downloads","my downloads"]
commands["open_documents"] = ["open documents","go to documents","documents folder","open documents folder","show documents","navigate to documents","my documents"]
commands["open_pictures"] = ["open pictures","go to pictures","pictures folder","open pictures folder","show pictures","navigate to pictures","my pictures","photos folder","open photos folder"]
commands["open_music"] = ["open music","go to music","music folder","open music folder","show music","navigate to music","my music"]
commands["open_videos"] = ["open videos","go to videos","videos folder","open videos folder","show videos","navigate to videos","my videos"]
commands["open_recycle_bin"] = ["open recycle bin","launch recycle bin","recycle bin","trash","open trash","show recycle bin"]
commands["open_temp"] = ["open temp folder","open temp","temp folder","temporary files","open temporary folder"]
commands["open_appdata"] = ["open appdata","appdata","app data","open app data","open application data"]
commands["open_program_files"] = ["open program files","program files","open programs","programs folder","navigate to program files"]
commands["open_system32"] = ["open system32","system32","open system folder","windows system folder"]
commands["open_startup_folder"] = ["open startup folder","startup folder","open startup","windows startup"]
commands["open_user_folder"] = ["open user folder","user folder","home folder","open home folder","open my folder","navigate to home"]
commands["open_c_drive"] = ["open c drive","c drive","local disk c","open local disk","go to c drive"]
commands["open_d_drive"] = ["open d drive","d drive","local disk d","go to d drive"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 10: WEBSITES — SEARCH & SOCIAL
# ══════════════════════════════════════════════════════════════
commands["open_google"] = ["open google","go to google","launch google","google","google.com","search engine","open search engine"]
commands["open_bing"] = ["open bing","go to bing","launch bing","bing","bing.com","microsoft search"]
commands["open_duckduckgo"] = ["open duckduckgo","go to duckduckgo","duckduckgo","duck duck go","open duck duck go"]
commands["open_github"] = ["open github","go to github","launch github","github","github.com","open code repository"]
commands["open_stackoverflow"] = ["open stackoverflow","go to stackoverflow","stackoverflow","stack overflow","open stack overflow"]
commands["open_reddit"] = ["open reddit","go to reddit","launch reddit","reddit","reddit.com"]
commands["open_twitter"] = ["open twitter","go to twitter","launch twitter","twitter","x","open x","go to x","x.com","twitter.com"]
commands["open_facebook"] = ["open facebook","go to facebook","launch facebook","facebook","fb","open fb","facebook.com"]
commands["open_instagram"] = ["open instagram","go to instagram","launch instagram","instagram","insta","open insta"]
commands["open_linkedin"] = ["open linkedin","go to linkedin","launch linkedin","linkedin","linked in","open linked in"]
commands["open_pinterest"] = ["open pinterest","go to pinterest","pinterest"]
commands["open_snapchat"] = ["open snapchat","go to snapchat","snapchat"]
commands["open_tiktok"] = ["open tiktok","go to tiktok","tiktok","tik tok","open tik tok"]
commands["open_quora"] = ["open quora","go to quora","quora"]
commands["open_medium"] = ["open medium","go to medium","medium","medium.com","open medium articles"]
commands["open_dev_to"] = ["open dev.to","go to dev.to","dev.to","dev to","open dev"]
commands["open_hashnode"] = ["open hashnode","go to hashnode","hashnode"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 11: WEBSITES — AI TOOLS
# ══════════════════════════════════════════════════════════════
commands["open_chatgpt"] = ["open chatgpt","go to chatgpt","chatgpt","chat gpt","open chat gpt","gpt","open gpt","openai chat","open openai"]
commands["open_claude"] = ["open claude","go to claude","claude","anthropic claude","open anthropic","claude ai"]
commands["open_gemini"] = ["open gemini","go to gemini","gemini","google gemini","bard","open bard","open google ai"]
commands["open_perplexity"] = ["open perplexity","go to perplexity","perplexity","perplexity ai","open perplexity ai"]
commands["open_copilot"] = ["open copilot","go to copilot","copilot","microsoft copilot","github copilot","open microsoft copilot"]
commands["open_grok"] = ["open grok","go to grok","grok","grok ai","open grok ai","xai grok"]
commands["open_mistral"] = ["open mistral","go to mistral","mistral","mistral ai","open mistral ai"]
commands["open_huggingface"] = ["open huggingface","go to huggingface","huggingface","hugging face","open hugging face"]
commands["open_midjourney"] = ["open midjourney","go to midjourney","midjourney","mid journey"]
commands["open_dalle"] = ["open dalle","go to dalle","dalle","dall-e","open dall-e","dall e","open image generator"]
commands["open_stable_diffusion"] = ["open stable diffusion","stable diffusion","stablediffusion","open sd"]
commands["open_runway"] = ["open runway","go to runway","runway","runway ml","open runway ml"]
commands["open_v0"] = ["open v0","go to v0","v0","v0.dev","vercel v0","open vercel v0"]
commands["open_bolt"] = ["open bolt","go to bolt","bolt","bolt.new","open bolt.new"]
commands["open_ollama"] = ["open ollama","go to ollama","ollama","ollama ai","open ollama website"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 12: WEBSITES — LEARNING & EDUCATION
# ══════════════════════════════════════════════════════════════
commands["open_wikipedia"] = ["open wikipedia","go to wikipedia","wikipedia","wiki","open wiki"]
commands["open_coursera"] = ["open coursera","go to coursera","coursera"]
commands["open_udemy"] = ["open udemy","go to udemy","udemy"]
commands["open_edx"] = ["open edx","go to edx","edx","open edx website"]
commands["open_khanacademy"] = ["open khan academy","go to khan academy","khan academy","khanacademy"]
commands["open_leetcode"] = ["open leetcode","go to leetcode","leetcode","leet code","coding practice"]
commands["open_hackerrank"] = ["open hackerrank","go to hackerrank","hackerrank","hacker rank"]
commands["open_codechef"] = ["open codechef","go to codechef","codechef","code chef"]
commands["open_codeforces"] = ["open codeforces","go to codeforces","codeforces","code forces"]
commands["open_geeksforgeeks"] = ["open geeksforgeeks","go to geeksforgeeks","geeksforgeeks","geeks for geeks","gfg","open gfg"]
commands["open_w3schools"] = ["open w3schools","go to w3schools","w3schools","w3 schools"]
commands["open_mdn"] = ["open mdn","go to mdn","mdn","mozilla developer network","mdn docs","open mozilla docs"]
commands["open_docs_python"] = ["open python docs","go to python docs","python docs","python documentation","python official docs"]
commands["open_npmjs"] = ["open npm","go to npm","npm","npmjs","open npmjs"]
commands["open_pypi"] = ["open pypi","go to pypi","pypi","python package index","open python packages"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 13: WEBSITES — PRODUCTIVITY & TOOLS
# ══════════════════════════════════════════════════════════════
commands["open_google_drive"] = ["open google drive","go to google drive","google drive","gdrive","open gdrive","open drive","drive","go to drive"]
commands["open_google_docs"] = ["open google docs","go to google docs","google docs","gdocs","open gdocs","open online docs"]
commands["open_google_sheets"] = ["open google sheets","go to google sheets","google sheets","gsheets","open gsheets","open online spreadsheet"]
commands["open_google_slides"] = ["open google slides","go to google slides","google slides","gslides","open online slides"]
commands["open_google_forms"] = ["open google forms","go to google forms","google forms","gforms"]
commands["open_google_calendar"] = ["open google calendar","go to google calendar","google calendar","gcal","open gcal"]
commands["open_google_meet"] = ["open google meet","go to google meet","google meet","gmeet","open gmeet"]
commands["open_google_translate"] = ["open google translate","go to google translate","google translate","translator","open translator","translate website"]
commands["open_pastebin"] = ["open pastebin","go to pastebin","pastebin","paste bin"]
commands["open_typeform"] = ["open typeform","go to typeform","typeform"]
commands["open_notion_website"] = ["open notion website","notion web","go to notion","notion.so"]
commands["open_airtable"] = ["open airtable","go to airtable","airtable","air table"]
commands["open_asana"] = ["open asana","go to asana","asana"]
commands["open_jira"] = ["open jira","go to jira","jira","open jira website"]
commands["open_clickup"] = ["open clickup","go to clickup","clickup","click up"]
commands["open_monday"] = ["open monday","go to monday","monday.com","open monday.com"]
commands["open_miro"] = ["open miro","go to miro","miro","miro board","open miro board"]
commands["open_figma_website"] = ["open figma website","figma web","go to figma.com","figma.com"]
commands["open_vercel"] = ["open vercel","go to vercel","vercel","vercel.com"]
commands["open_netlify"] = ["open netlify","go to netlify","netlify"]
commands["open_replit"] = ["open replit","go to replit","replit","repl.it","open repl"]
commands["open_codepen"] = ["open codepen","go to codepen","codepen","code pen"]
commands["open_codesandbox"] = ["open codesandbox","go to codesandbox","codesandbox","code sandbox"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 14: WEBSITES — NEWS & INFO
# ══════════════════════════════════════════════════════════════
commands["open_news_google"] = ["open google news","go to google news","google news","news","open news","show news"]
commands["open_bbc"] = ["open bbc","go to bbc","bbc","bbc news","open bbc news"]
commands["open_cnn"] = ["open cnn","go to cnn","cnn","cnn news","open cnn news"]
commands["open_ndtv"] = ["open ndtv","go to ndtv","ndtv","ndtv news","open ndtv news"]
commands["open_timesofindia"] = ["open times of india","go to times of india","times of india","toi","open toi"]
commands["open_hindustantimes"] = ["open hindustan times","hindustan times","ht","open ht news"]
commands["open_thehindu"] = ["open the hindu","the hindu","go to the hindu"]
commands["open_techcrunch"] = ["open techcrunch","go to techcrunch","techcrunch","tech crunch","open tech news"]
commands["open_theverge"] = ["open the verge","the verge","go to the verge","verge tech news"]
commands["open_wired"] = ["open wired","go to wired","wired","wired news"]
commands["open_hackernews"] = ["open hacker news","go to hacker news","hacker news","hn","open hn"]
commands["open_producthunt"] = ["open product hunt","go to product hunt","product hunt","producthunt"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 15: SEARCH COMMANDS
# ══════════════════════════════════════════════════════════════
commands["search_google"] = ["search google","google search","search on google","look up on google","find on google","search the web","web search","search internet","google for","find on web","lookup","search for"]
commands["search_youtube"] = ["search youtube","youtube search","search on youtube","look up on youtube","find on youtube","find video","search video","search for video on youtube","youtube for"]
commands["search_wikipedia"] = ["search wikipedia","wikipedia search","search on wikipedia","look up on wikipedia","find on wikipedia","wiki search","search wiki","find on wiki","lookup wikipedia"]
commands["search_google_images"] = ["search google images","google images search","image search","search images","find images","look up images","search for images","find pictures online"]
commands["search_amazon"] = ["search amazon","amazon search","search on amazon","look up on amazon","find on amazon","shop on amazon","buy on amazon"]
commands["search_flipkart"] = ["search flipkart","flipkart search","search on flipkart","look up on flipkart","find on flipkart","shop on flipkart"]
commands["search_stackoverflow"] = ["search stackoverflow","stackoverflow search","search on stackoverflow","look up on stackoverflow","find answer on stackoverflow"]
commands["search_github"] = ["search github","github search","search on github","find on github","look up on github","find repository","search repo","find repo"]
commands["search_news"] = ["search news","news search","search for news","look up news","find news","recent news on","latest news about","news about"]
commands["search_maps"] = ["search maps","google maps","find location","search location","navigate to","directions to","find on map","open maps search","map search"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 16: SCREENSHOT & SCREEN RECORDING
# ══════════════════════════════════════════════════════════════
commands["take_screenshot"] = ["take screenshot","capture screenshot","screenshot","grab screenshot","take screen capture","capture screen","screen capture","take snap","screen snap","take a screenshot","click screenshot","save screenshot","printscreen"]
commands["screenshot_window"] = ["screenshot active window","capture active window","screenshot current window","capture window","screen capture window"]
commands["screenshot_region"] = ["screenshot region","capture region","screenshot area","capture area","partial screenshot","select area screenshot"]
commands["start_screen_recording"] = ["start screen recording","record screen","screen record","begin screen recording","record my screen","capture screen video","record desktop"]
commands["stop_screen_recording"] = ["stop screen recording","stop recording","end screen recording","finish recording","stop capturing screen"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 17: CLIPBOARD
# ══════════════════════════════════════════════════════════════
commands["show_clipboard"] = ["show clipboard","open clipboard","clipboard","clipboard history","show clipboard history","open clipboard manager","view clipboard"]
commands["clear_clipboard"] = ["clear clipboard","empty clipboard","delete clipboard","wipe clipboard","reset clipboard"]
commands["copy_last"] = ["copy last","copy previous","copy that again","copy it again"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 18: VOLUME CONTROL
# ══════════════════════════════════════════════════════════════
commands["volume_up"] = ["volume up","increase volume","turn up volume","raise volume","louder","make louder","boost volume","volume higher","sound up","increase sound","turn up sound","raise sound"]
commands["volume_down"] = ["volume down","decrease volume","turn down volume","lower volume","quieter","make quieter","reduce volume","volume lower","sound down","decrease sound","turn down sound","lower sound","softer"]
commands["volume_mute"] = ["mute","mute volume","mute sound","silence","silent mode","turn off sound","no sound","disable sound","mute audio","turn off audio","audio off","mute speakers"]
commands["volume_unmute"] = ["unmute","unmute volume","unmute sound","turn on sound","enable sound","restore sound","sound on","audio on","unmute audio","turn on audio","speakers on"]
commands["volume_max"] = ["max volume","maximum volume","full volume","volume full","volume 100","loudest","set max volume","crank up volume","volume to max"]
commands["volume_min"] = ["min volume","minimum volume","volume zero","volume 0","lowest volume","set min volume","volume to minimum"]
commands["volume_50"] = ["volume 50","set volume 50","half volume","medium volume","volume half","50 percent volume"]
commands["open_volume_mixer"] = ["open volume mixer","volume mixer","sound mixer","open sound mixer","audio mixer","open audio settings","sound settings","volume settings"]
commands["open_sound_settings"] = ["open sound settings","sound settings","audio settings","open audio settings","sound control panel","open sound control","audio control"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 19: BRIGHTNESS CONTROL
# ══════════════════════════════════════════════════════════════
commands["brightness_up"] = ["brightness up","increase brightness","turn up brightness","raise brightness","brighter","make brighter","higher brightness","screen brighter"]
commands["brightness_down"] = ["brightness down","decrease brightness","turn down brightness","lower brightness","dimmer","make dimmer","reduce brightness","lower screen brightness","screen dimmer"]
commands["brightness_max"] = ["max brightness","maximum brightness","full brightness","brightness full","brightness 100","brightest"]
commands["brightness_min"] = ["min brightness","minimum brightness","brightness zero","lowest brightness","darkest","dim screen","dark screen"]
commands["brightness_50"] = ["brightness 50","set brightness 50","half brightness","medium brightness","50 percent brightness"]
commands["night_light_on"] = ["turn on night light","night light on","enable night light","night mode","blue light filter","enable blue light filter","warm screen"]
commands["night_light_off"] = ["turn off night light","night light off","disable night light","disable night mode","disable blue light filter","normal screen color"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 20: MEDIA PLAYBACK
# ══════════════════════════════════════════════════════════════
commands["media_play"] = ["play","play music","start music","play media","resume music","resume playback","resume media","unpause","unpause music","continue music","start playback"]
commands["media_pause"] = ["pause","pause music","stop music","pause media","pause playback","halt music","pause song","pause audio","hold music"]
commands["media_stop"] = ["stop","stop music","stop media","stop playback","end playback","halt playback"]
commands["media_next"] = ["next song","next track","skip song","skip track","play next","next music","forward track","skip forward","next","next music track"]
commands["media_previous"] = ["previous song","previous track","last song","go back song","back track","play previous","previous music","rewind track","previous","prev song","last track"]
commands["media_shuffle"] = ["shuffle","shuffle music","enable shuffle","turn on shuffle","random music","play random","shuffle songs","randomize"]
commands["media_repeat"] = ["repeat","repeat music","loop music","enable repeat","turn on repeat","loop song","repeat track","loop track"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 21: SYSTEM POWER
# ══════════════════════════════════════════════════════════════
commands["shutdown"] = ["shutdown","shut down","shut down pc","shut down computer","shutdown pc","shutdown computer","turn off pc","turn off computer","power off","power off pc","power off computer","switch off pc","switch off computer","close down","system shutdown","shutdown system"]
commands["restart"] = ["restart","restart pc","restart computer","reboot","reboot pc","reboot computer","restart system","system restart","restart windows","reboot windows","restart machine"]
commands["sleep"] = ["sleep","sleep pc","sleep computer","sleep mode","put to sleep","go to sleep","enter sleep mode","suspend","suspend pc","hibernate sleep","standby","standby mode"]
commands["hibernate"] = ["hibernate","hibernate pc","hibernate computer","hibernation mode","deep sleep","hibernate system","enable hibernation"]
commands["lock"] = ["lock","lock pc","lock computer","lock screen","lock workstation","lock windows","secure screen","screen lock","lock system","lock my pc"]
commands["logoff"] = ["log off","logoff","sign out","sign out windows","sign out pc","logout","log out","logout pc","log out of windows","end session"]
commands["switch_user"] = ["switch user","change user","switch account","change account","new user session","open login screen"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 22: TASK MANAGER & SYSTEM TOOLS
# ══════════════════════════════════════════════════════════════
commands["open_task_manager"] = ["open task manager","task manager","launch task manager","taskmgr","open taskmgr","processes","open processes","running tasks","show processes","show running apps","kill processes"]
commands["open_resource_monitor"] = ["open resource monitor","resource monitor","launch resource monitor","resmon","system monitor","performance monitor"]
commands["open_performance_monitor"] = ["open performance monitor","performance monitor","perfmon","system performance","launch performance monitor"]
commands["open_event_viewer"] = ["open event viewer","event viewer","launch event viewer","eventvwr","system events","windows logs"]
commands["open_device_manager"] = ["open device manager","device manager","launch device manager","devmgmt","manage devices","hardware manager"]
commands["open_disk_management"] = ["open disk management","disk management","diskmgmt","manage disks","partition manager"]
commands["open_registry"] = ["open registry","registry","regedit","open regedit","launch registry","windows registry","registry editor"]
commands["open_gpedit"] = ["open group policy","group policy","gpedit","launch gpedit","group policy editor","local policy"]
commands["open_services"] = ["open services","services","launch services","windows services","service manager","services.msc"]
commands["open_msc"] = ["open msc","computer management","compmgmt","open computer management","launch computer management"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 23: CONTROL PANEL & SETTINGS
# ══════════════════════════════════════════════════════════════
commands["open_settings"] = ["open settings","windows settings","settings","system settings","launch settings","go to settings","open windows settings","preferences"]
commands["open_control_panel"] = ["open control panel","control panel","launch control panel","cpanel","system control panel","windows control panel"]
commands["open_display_settings"] = ["open display settings","display settings","screen settings","resolution settings","monitor settings","screen resolution","open screen settings"]
commands["open_personalization"] = ["open personalization","personalization settings","customize windows","desktop settings","open theme settings","theme settings","wallpaper settings","open wallpaper settings"]
commands["open_apps_settings"] = ["open apps settings","apps settings","installed apps","open installed apps","manage apps","uninstall apps","programs and features"]
commands["open_update_settings"] = ["open update settings","windows update","update settings","check for updates","windows updates","open updates","update windows"]
commands["open_security_settings"] = ["open security settings","security settings","windows security","defender settings","open windows security","antivirus settings","firewall settings"]
commands["open_privacy_settings"] = ["open privacy settings","privacy settings","windows privacy","open privacy","manage privacy"]
commands["open_network_settings"] = ["open network settings","network settings","wifi settings","network and internet","open network","internet settings","connection settings"]
commands["open_bluetooth_settings"] = ["open bluetooth settings","bluetooth settings","manage bluetooth","bluetooth","pair bluetooth","open bluetooth","bluetooth devices"]
commands["open_mouse_settings"] = ["open mouse settings","mouse settings","cursor settings","pointer settings","mouse control panel"]
commands["open_keyboard_settings"] = ["open keyboard settings","keyboard settings","input settings","keyboard control panel"]
commands["open_printer_settings"] = ["open printer settings","printer settings","printers","manage printers","printer and scanner","add printer"]
commands["open_user_accounts"] = ["open user accounts","user accounts","manage accounts","account settings","open accounts"]
commands["open_date_time_settings"] = ["open date time settings","date time settings","clock settings","time settings","open time settings","time and date","adjust date time"]
commands["open_language_settings"] = ["open language settings","language settings","region settings","locale settings","language and region"]
commands["open_ease_of_access"] = ["open ease of access","ease of access","accessibility settings","open accessibility","accessibility"]
commands["open_power_settings"] = ["open power settings","power settings","power options","battery settings","energy settings","power management"]
commands["open_storage_settings"] = ["open storage settings","storage settings","disk cleanup","storage sense","storage management","free up space"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 24: NETWORK & INTERNET
# ══════════════════════════════════════════════════════════════
commands["wifi_on"] = ["turn on wifi","wifi on","enable wifi","connect wifi","turn on wireless","wireless on","enable wireless","start wifi","activate wifi"]
commands["wifi_off"] = ["turn off wifi","wifi off","disable wifi","disconnect wifi","turn off wireless","wireless off","disable wireless","stop wifi","deactivate wifi"]
commands["bluetooth_on"] = ["turn on bluetooth","bluetooth on","enable bluetooth","start bluetooth","activate bluetooth"]
commands["bluetooth_off"] = ["turn off bluetooth","bluetooth off","disable bluetooth","stop bluetooth","deactivate bluetooth"]
commands["airplane_mode_on"] = ["airplane mode on","enable airplane mode","turn on airplane mode","flight mode on","enable flight mode"]
commands["airplane_mode_off"] = ["airplane mode off","disable airplane mode","turn off airplane mode","flight mode off","disable flight mode"]
commands["check_internet"] = ["check internet","check connection","internet speed","test internet","internet status","check wifi status","am i connected","ping test","check network"]
commands["open_network_connections"] = ["open network connections","network connections","show connections","network adapters","open adapters"]
commands["vpn_connect"] = ["connect vpn","enable vpn","turn on vpn","vpn on","start vpn","activate vpn"]
commands["vpn_disconnect"] = ["disconnect vpn","disable vpn","turn off vpn","vpn off","stop vpn","deactivate vpn"]
commands["flush_dns"] = ["flush dns","clear dns","refresh dns","dns flush","reset dns","clear dns cache"]
commands["ipconfig"] = ["show ip","ipconfig","my ip address","ip address","show network info","network info","what is my ip","check ip"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 25: SYSTEM INFO
# ══════════════════════════════════════════════════════════════
commands["system_info"] = ["system info","system information","computer info","computer information","about my pc","pc info","open system info","show system info","about this pc","pc specs","computer specs","hardware info","system specs"]
commands["battery_status"] = ["battery status","check battery","battery level","how much battery","battery percentage","battery info","power status","laptop battery"]
commands["cpu_usage"] = ["cpu usage","processor usage","cpu load","processor load","show cpu","check cpu","how much cpu","cpu performance"]
commands["ram_usage"] = ["ram usage","memory usage","how much ram","check ram","ram status","memory status","show memory","memory info","free memory"]
commands["disk_usage"] = ["disk usage","storage usage","disk space","check disk","free space","disk status","how much space","storage info","show disk space"]
commands["gpu_info"] = ["gpu info","graphics info","video card info","gpu status","graphics card status","check gpu","show gpu"]
commands["uptime"] = ["system uptime","how long running","uptime","computer uptime","show uptime","pc uptime","running time"]
commands["windows_version"] = ["windows version","os version","what windows version","which windows","winver","open winver","show windows version"]
commands["check_temp"] = ["check temperature","cpu temperature","system temperature","thermal status","how hot is cpu","temperature check"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 26: DATE & TIME
# ══════════════════════════════════════════════════════════════
commands["what_time"] = ["what time is it","what is the time","current time","show time","tell me the time","time now","time","clock","what time","check time","time please"]
commands["what_date"] = ["what is the date","current date","today date","today's date","what day is it","show date","tell me the date","date","date today","what date","check date"]
commands["what_day"] = ["what day is today","which day is today","today is which day","day today","current day","today day"]
commands["what_year"] = ["what year is it","current year","this year","which year","year now"]
commands["set_alarm"] = ["set alarm","create alarm","new alarm","add alarm","alarm for","set an alarm","remind me at","wake me up at","alarm at"]
commands["set_timer"] = ["set timer","create timer","start timer","timer for","new timer","countdown timer","count down","set countdown","start countdown for"]
commands["set_reminder"] = ["set reminder","create reminder","remind me","reminder for","new reminder","add reminder","remind me to","set a reminder"]
commands["show_alarms"] = ["show alarms","list alarms","my alarms","all alarms","view alarms","open alarms"]
commands["world_clock"] = ["world clock","open world clock","time in","what time in","timezone","different timezone","clock for city"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 27: FILE OPERATIONS
# ══════════════════════════════════════════════════════════════
commands["create_folder"] = ["create folder","make folder","new folder","create directory","make directory","new directory","create new folder","mkdir","make new folder","add folder"]
commands["delete_file"] = ["delete file","remove file","trash file","move to trash","delete","remove","get rid of file","erase file"]
commands["rename_file"] = ["rename file","rename","change name","rename folder","change file name","give new name"]
commands["copy_file"] = ["copy file","copy","duplicate file","make copy","clone file","copy folder","duplicate folder"]
commands["move_file"] = ["move file","move","cut file","relocate file","transfer file","move folder","relocate folder"]
commands["search_file"] = ["search file","find file","look for file","search for file","locate file","where is file","find document","look up file","search document","find folder","locate folder","search files","file search"]
commands["open_file"] = ["open file","open document","launch file","view file","run file","open this file","open that file"]
commands["zip_file"] = ["zip file","compress file","create zip","zip folder","compress folder","archive file","create archive","zip it","compress it"]
commands["unzip_file"] = ["unzip file","extract file","unzip","extract zip","decompress file","extract archive","unpack file","extract folder"]
commands["properties"] = ["file properties","show properties","properties","folder properties","check properties","view properties","file info","file details"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 28: WINDOW MANAGEMENT
# ══════════════════════════════════════════════════════════════
commands["minimize_window"] = ["minimize window","minimize","minimize current window","minimize this window","shrink window","hide window","minimize app","shrink to taskbar"]
commands["maximize_window"] = ["maximize window","maximize","maximize current window","maximize this window","full screen","fullscreen","expand window","make full screen"]
commands["restore_window"] = ["restore window","restore","restore current window","restore this window","windowed mode","exit full screen","normal window"]
commands["close_window"] = ["close window","close","close current window","close this window","close app","close application","shut window","exit window","close tab"]
commands["switch_window"] = ["switch window","switch app","alt tab","next window","change window","task switcher","app switcher","window switcher","switch between apps"]
commands["snap_left"] = ["snap left","window left","move window left","align left","dock left","snap to left","put window left"]
commands["snap_right"] = ["snap right","window right","move window right","align right","dock right","snap to right","put window right"]
commands["snap_top"] = ["snap top","snap maximize","window top","maximize snap","snap to top"]
commands["snap_bottom"] = ["snap bottom","window bottom","snap to bottom","half screen bottom"]
commands["virtual_desktop_new"] = ["new virtual desktop","create virtual desktop","new desktop","add desktop","open new desktop","virtual desktop"]
commands["virtual_desktop_next"] = ["next virtual desktop","switch desktop","change desktop","next desktop","go to next desktop","virtual desktop next"]
commands["show_all_windows"] = ["show all windows","task view","all windows","window overview","mission control","show open apps","open apps","all open apps"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 29: KEYBOARD SHORTCUTS (AS COMMANDS)
# ══════════════════════════════════════════════════════════════
commands["do_undo"] = ["undo","undo that","undo last","ctrl z","reverse last action","undo action","take back that","un-do"]
commands["do_redo"] = ["redo","redo that","redo last","ctrl y","redo action","do again","redo it"]
commands["do_copy"] = ["copy","copy this","copy that","copy selected","copy text","ctrl c","copy selection"]
commands["do_paste"] = ["paste","paste this","paste that","paste text","ctrl v","paste it","paste here"]
commands["do_cut"] = ["cut","cut this","cut that","cut selected","cut text","ctrl x","cut selection"]
commands["do_select_all"] = ["select all","ctrl a","select everything","highlight all","select all text"]
commands["do_save"] = ["save","save file","ctrl s","save document","save this","save now","save changes"]
commands["do_save_as"] = ["save as","ctrl shift s","save as new","save copy","save to new file"]
commands["do_find"] = ["find","find text","ctrl f","search in document","find in file","open find","search this page"]
commands["do_print"] = ["print","print this","print document","ctrl p","open print dialog","print file","print page"]
commands["do_refresh"] = ["refresh","reload","ctrl r","f5","refresh page","reload page","refresh browser","refresh window"]
commands["do_new"] = ["new","new file","ctrl n","open new","create new","new document","new tab","open new tab","add new tab"]
commands["do_open"] = ["open","open dialog","ctrl o","open file dialog","browse file","pick file"]
commands["do_close_tab"] = ["close tab","ctrl w","close this tab","shut tab","remove tab"]
commands["do_reopen_tab"] = ["reopen tab","ctrl shift t","reopen closed tab","restore tab","bring back tab"]
commands["do_zoom_in"] = ["zoom in","make bigger","ctrl plus","increase zoom","zoom up","larger text","bigger screen"]
commands["do_zoom_out"] = ["zoom out","make smaller","ctrl minus","decrease zoom","zoom down","smaller text","smaller screen"]
commands["do_zoom_reset"] = ["reset zoom","default zoom","ctrl 0","normal zoom","zoom 100","restore zoom"]
commands["do_fullscreen"] = ["fullscreen","full screen mode","f11","toggle fullscreen","browser fullscreen"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 30: AI & MEMORY COMMANDS
# ══════════════════════════════════════════════════════════════
commands["remember_this"] = ["remember this","remember that","save this","store this","note this","keep this","remember","memorize this","don't forget this","keep note","make note","save to memory","add to memory","remember it","store in memory"]
commands["what_do_you_know"] = ["what do you know","show memory","show what you know","what do you remember","show stored info","memory dump","show my memories","what have you saved","what have you remembered"]
commands["forget_this"] = ["forget this","forget that","delete memory","remove from memory","clear this memory","erase memory","forget it","forget everything"]
commands["set_goal"] = ["set goal","add goal","new goal","save goal","store goal","my goal is","remember my goal","goal is","create goal"]
commands["show_goals"] = ["show goals","my goals","list goals","what are my goals","show my goals","open goals","view goals"]
commands["set_preference"] = ["set preference","save preference","i prefer","my preference is","remember preference","store preference","i like","i dislike","i want"]
commands["show_preferences"] = ["show preferences","my preferences","list preferences","what are my preferences","show my preferences"]
commands["ai_chat"] = ["chat with ai","talk to ai","ai conversation","open ai chat","start ai conversation","think","analyze","explain","what is","who is","how to","tell me about","can you","help me","i need","i want to know"]
commands["ai_summarize"] = ["summarize","summarize this","give me summary","summarize for me","tldr","brief me","brief summary","short summary","quick summary"]
commands["ai_analyze"] = ["analyze","analyse","analyze this","deep analysis","detailed analysis","explain in detail","break it down","break this down"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 31: DOCUMENT COMMANDS
# ══════════════════════════════════════════════════════════════
commands["open_pdf"] = ["open pdf","read pdf","view pdf","open this pdf","launch pdf","pdf viewer","open pdf file","read this pdf","show pdf"]
commands["summarize_document"] = ["summarize document","summarize file","document summary","file summary","summarize pdf","summarize docx","summarize this file","summarize this document","give summary of document"]
commands["search_document"] = ["search in document","find in document","search document","look in document","find in file","search in file","keyword in document","find keyword","search inside document"]
commands["read_document"] = ["read document","read file","read this","read aloud","read out","read to me","read this file","read this document"]
commands["extract_text"] = ["extract text","get text","copy text from","text extraction","extract from pdf","extract content","get content from"]
commands["compare_documents"] = ["compare documents","compare files","compare these","difference between files","doc comparison","file comparison","diff files"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 32: INTERNET RESEARCH
# ══════════════════════════════════════════════════════════════
commands["web_research"] = ["research","do research","search the web","research this","web research","find information","gather info","look up information","find info about","research topic","investigate","what is the latest","find me information on"]
commands["check_weather"] = ["weather","check weather","what is the weather","today weather","weather today","weather forecast","what weather","how is the weather","weather outside","current weather","is it raining","temperature outside","weather report","what temperature","weather update"]
commands["check_stocks"] = ["check stocks","stock price","share price","market price","nifty","sensex","check nifty","check sensex","stock market","market today","stock update","market update","share market","check share price","crypto price"]
commands["get_news"] = ["get news","latest news","current news","news today","today news","recent news","breaking news","top news","news update","fetch news","show news"]
commands["translate"] = ["translate","translate this","translation","translate to","convert language","translate from","language translation","translate text","translate word","meaning in"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 33: CALCULATOR & MATH
# ══════════════════════════════════════════════════════════════
commands["calculate"] = ["calculate","compute","math","solve","what is","how much is","add","subtract","multiply","divide","percentage","plus","minus","times","divided by","equals","evaluate","sum","total","result of","answer to","calculate this","solve this","do the math"]
commands["unit_convert"] = ["convert","unit conversion","convert units","change units","convert to","in meters","in feet","in kg","in pounds","convert temperature","celsius to fahrenheit","fahrenheit to celsius","km to miles","miles to km"]
commands["currency_convert"] = ["currency convert","exchange rate","convert currency","inr to usd","usd to inr","dollar to rupee","rupee to dollar","eur to inr","convert money","how much in","foreign exchange"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 34: UTILITY & MISC
# ══════════════════════════════════════════════════════════════
commands["open_run"] = ["open run","run dialog","run command","win r","open run dialog","run box","execute command"]
commands["open_search"] = ["open search","windows search","search windows","win s","taskbar search","find app","start menu search"]
commands["open_action_center"] = ["open action center","action center","notification center","notifications","open notifications","show notifications","open notification panel"]
commands["open_task_view"] = ["open task view","task view","all desktops","open task overview","timeline","windows timeline"]
commands["open_emoji"] = ["open emoji","emoji picker","insert emoji","emoji keyboard","emoji panel","win period","emoji window"]
commands["open_snip_sketch"] = ["open snip and sketch","snip and sketch","screen sketch","annotate screen","markup screen"]
commands["open_steps_recorder"] = ["open steps recorder","steps recorder","record steps","psr","problem steps recorder"]
commands["open_magnifier"] = ["open magnifier","magnifier","zoom screen","screen magnifier","screen zoom","enlarge screen"]
commands["open_narrator"] = ["open narrator","narrator","text to speech screen","screen reader","read screen"]
commands["open_on_screen_keyboard"] = ["on screen keyboard","open keyboard","virtual keyboard","touch keyboard","osk"]
commands["dark_mode"] = ["dark mode","enable dark mode","turn on dark mode","dark theme","switch to dark","night theme","dark interface","black theme"]
commands["light_mode"] = ["light mode","enable light mode","turn on light mode","light theme","switch to light","day theme","white theme","bright mode"]
commands["do_not_disturb"] = ["do not disturb","dnd","focus mode","quiet hours","silence notifications","mute notifications","block notifications","enable focus","enable dnd"]
commands["show_desktop"] = ["show desktop","minimize all","hide all windows","go to desktop","minimize all windows","clear desktop","desktop view","win d"]
commands["open_startup_apps"] = ["open startup apps","startup apps","manage startup","startup programs","boot apps","apps on startup","startup manager"]
commands["format_drive"] = ["format drive","format disk","format usb","format partition","erase drive","wipe drive","reformat drive"]
commands["defragment"] = ["defragment","defrag","optimize drive","disk defrag","disk optimization","optimize disk"]
commands["disk_cleanup"] = ["disk cleanup","clean disk","free disk space","delete temp files","clean up disk","clear disk","storage cleanup","clean junk","remove junk files","clear junk","clean up storage"]
commands["check_disk"] = ["check disk","chkdsk","disk check","scan disk","check for errors","disk error check","scan for disk errors"]
commands["system_restore"] = ["system restore","restore point","create restore point","go back to restore point","undo system changes"]
commands["open_firewall"] = ["open firewall","windows firewall","firewall settings","open firewall settings","manage firewall","firewall control"]
commands["open_defender"] = ["open defender","windows defender","antivirus","open antivirus","security scan","virus scan","defender settings","open windows defender"]
commands["scan_virus"] = ["scan for virus","virus scan","malware scan","check for virus","antivirus scan","security scan","scan computer","full scan","quick scan"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 35: GAMING
# ══════════════════════════════════════════════════════════════
commands["open_steam"] = ["open steam","launch steam","steam","steam games","open steam client"]
commands["open_epic_games"] = ["open epic games","launch epic games","epic games","epic games launcher","open epic","epic store"]
commands["open_origin"] = ["open origin","launch origin","origin","origin games","ea games","open ea"]
commands["open_uplay"] = ["open uplay","launch uplay","uplay","ubisoft connect","open ubisoft"]
commands["open_gog"] = ["open gog","launch gog","gog","gog galaxy","open gog galaxy"]
commands["open_battle_net"] = ["open battle.net","battle.net","battlenet","open battlenet","blizzard launcher"]
commands["open_minecraft"] = ["open minecraft","launch minecraft","minecraft","start minecraft"]
commands["open_roblox"] = ["open roblox","launch roblox","roblox","start roblox"]
commands["open_game_bar"] = ["open game bar","game bar","xbox game bar","overlay","game overlay","win g","gaming overlay"]
commands["start_game_recording"] = ["start game recording","record gameplay","record game","game capture","capture gameplay","record this game"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 36: SECURITY & PRIVACY
# ══════════════════════════════════════════════════════════════
commands["clear_browser_history"] = ["clear history","delete browser history","clear browsing history","erase history","remove history","wipe history","delete history","clear browser data"]
commands["clear_cache"] = ["clear cache","delete cache","remove cache","clean cache","wipe cache","clear temp files","clear cookies","delete cookies","remove cookies"]
commands["password_manager"] = ["open password manager","password manager","passwords","my passwords","saved passwords","manage passwords"]
commands["private_mode"] = ["private mode","incognito","incognito mode","private browsing","open private window","open incognito","open incognito window"]
commands["clear_downloads_history"] = ["clear downloads history","delete download history","clear download list","remove download history"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 37: ACCESSIBILITY
# ══════════════════════════════════════════════════════════════
commands["high_contrast"] = ["high contrast mode","enable high contrast","turn on high contrast","high contrast theme","accessibility contrast","contrast mode"]
commands["sticky_keys"] = ["sticky keys","enable sticky keys","turn on sticky keys","accessibility keys"]
commands["filter_keys"] = ["filter keys","enable filter keys","turn on filter keys"]
commands["toggle_caps_lock"] = ["caps lock","toggle caps","enable caps lock","disable caps lock","turn on caps lock","turn off caps lock","capital letters"]

# ══════════════════════════════════════════════════════════════
# CATEGORY 38: TORVAK SYSTEM COMMANDS
# ══════════════════════════════════════════════════════════════
commands["torvak_exit"] = ["exit","quit","goodbye","bye","close torvak","exit torvak","quit torvak","stop torvak","shutdown torvak","turn off torvak","end session","close assistant","quit assistant","exit assistant","done","that's all","all done","see you","farewell"]
commands["torvak_help"] = ["help","what can you do","show commands","list commands","commands","available commands","how to use","guide","manual","help me","show help","what do you support","supported commands","show me what you can do","capabilities"]
commands["torvak_status"] = ["status","system status","torvak status","how are you","are you running","are you there","check status","assistant status","are you active"]
commands["torvak_clear"] = ["clear","clear chat","clear conversation","clear screen","wipe chat","reset chat","new conversation","fresh start","clear history","wipe screen"]
commands["torvak_repeat"] = ["repeat","say that again","repeat that","what did you say","again","repeat last","what was that","can you repeat","say again"]
commands["torvak_louder"] = ["speak louder","louder please","increase voice","voice louder","speak up","can't hear you","louder voice","tts louder","assistant louder"]
commands["torvak_softer"] = ["speak softer","softer please","decrease voice","voice softer","quiet voice","lower voice","tts softer","assistant softer","speak quietly"]
commands["torvak_reload"] = ["reload torvak","restart torvak","refresh torvak","reinitialize","reload assistant","restart assistant","reset torvak","torvak reload"]
commands["torvak_settings"] = ["torvak settings","open settings torvak","configure torvak","assistant settings","torvak config","torvak preferences","configure assistant"]
commands["torvak_version"] = ["torvak version","what version","version number","build version","software version","which version","current version","version info"]
commands["torvak_update"] = ["update torvak","check for update","torvak update","new version available","upgrade torvak","install update","update assistant"]

