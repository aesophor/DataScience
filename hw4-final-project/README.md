從 Data Science 看 Google, Apple, Facebook 對軟體工程師的需求
---
Authors: 資科二 [張育甄](https://github.com/a19990506)、資科二 [許宸禎](https://github.com/aarriiel)、資科三 [王冠中](https://github.com/aesophor)

> 在大學四年的訓練中，我們學了很多 Computer Science 的課程，也接受了許多程式訓練。但業界需求和學校所學可能有極大落差，因此我們決定用 Web Scraper 爬出 Google, Apple, Facebook 等公司的 Job Descriptions 並進行統計分析。

* 進 Google, Apple, Facebook 一定要高學歷？
* 一定要有5年以上豐富經驗？
* 軟體工程師是最夯職缺？
* 如果只是想進大公司，應該學什麼程式語言、Framework，CP值最高？
* 畢業後究竟該留在國內，還是到國外賺得比臺灣多？

**讓我們實際地分析資料破除上述迷思！！**

以下分析資料來源：各公司網站公開的Job Descriptions. Google（1710筆）, Apple（2148筆）, Facebook（1067筆）。    
搜集時間：2019/01/22    
分析結果僅供參考。

![](https://i.imgur.com/KNFJ3Tg.png)

---
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/1200px-Google_2015_logo.svg.png" width="150">

**1. Google 學歷要求**
![](https://i.imgur.com/imfFohS.png) 
很多人對大公司的印象就是，要有很高的學歷才能找到那裏的工作。但上圖顯示，雖然 Google 傾向錄取碩士（Master）學歷的 candidate，但實際上多數的職缺都只要求大學（Bachelor）學歷即可，甚至有些職缺沒列出學歷要求。

**2. Google 經驗要求**
![](https://i.imgur.com/Gyb57X7.png)
從上述圖表可以看見 Google 大部分的工作其實也沒有經驗要求，大多數職缺的門檻並沒有想像中的高。有豐富的經驗可能會讓一個人的創意被局限，反觀剛畢業的社會新鮮人，他們可能對技術上手快、應用能力強、腦袋靈活、能跳脫窠臼。

**3. Google 需求最大的職缺**
![](https://i.imgur.com/Ep4qsy6.png)
資料顯示，Google全球職缺中，需求量最高的是 Software Engineer。

**4. Google 最值得學的 Programming Languages / Frameworks / Skills**
![](https://i.imgur.com/9cBGHUC.png)
![](https://i.imgur.com/CMTSXNs.png)
![](https://i.imgur.com/SHqUmhW.png)
目前 Google 徵才以懂 Java, Python, C++, Go 等語言的人才爲主。在 minimum/preferred qualifications 與 responsibilities 敘述所產生的文字雲中，物件導向、JSP、ASP、XAML、XUL、GWT、Flex ...等，可能是在 Google 工作會用到的技術/框架。

---

<img src="https://www.apple.com/ac/structured-data/images/knowledge_graph_logo.png?201606271147" width="75">

**1. Apple 學歷要求**

![](https://i.imgur.com/WnMrREt.png)
和 Google 不同的是：Apple 要求 BS(Bachelor of Science)，而 Google 僅要求大學畢業並未指定一定要理學士。

**2. Apple 經驗要求**

![](https://i.imgur.com/OBcLdTs.png)
大多職缺沒有指定需要幾年經驗。

**3. Apple 需求最大的職缺**

![](https://i.imgur.com/gYEtyTm.png)
仍然以 Software Engineer 爲主。

**4. Apple 最值得學的 Programming Languages / Frameworks / Skills**

![](https://i.imgur.com/0XPNKYh.png)
![](https://i.imgur.com/5HQZKns.png)
![](https://i.imgur.com/OuwUYaL.png)
三大基本要求還是 Java, Python, C++。而在這裏可見 Apple 偏好懂 Swift 語言的軟體工程師。

---

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Facebook_logo_%28square%29.png/900px-Facebook_logo_%28square%29.png" width="75">

**1. 學歷要求**

![](https://i.imgur.com/iBD2zdc.png)
許多職缺並沒有列出學歷要求，Preferred Qualifications 學歷要求分布相當平均。

**2. 經驗要求**

![](https://i.imgur.com/l3vprsr.png)
許多職缺不要求經驗。

**3. 需求最大的職缺**

![](https://i.imgur.com/MAz6J9z.png)
還是 Software Engineer 爲主。

**4. 最值得學的 Programming Languages / Frameworks / Skills**

![](https://i.imgur.com/MwIZl1O.png)
![](https://i.imgur.com/Mi2vvny.png)
![](https://i.imgur.com/pOUcZVT.png)
三大基本要求還是 Java, Python, C++。除此之外 Facebook 也特別傾向 Php, SQL 技術。    
從文字雲中可看見 low-level 一詞，到 github.com/facebook 可看見許多底層的程式專案，如：folly, watchman, redex, ...etc. 

---

## 小結
縱觀上述資料的分析結果，若想到 Google, Apple, Facebook 等大公司工作，建議具備一下能力：
* Programming Languages: `C++/Java/Python` （擇一精通） + `Go` (Google), `Swift` (Apple), `Php+SQL` (Facebook)
* Frameworks: `JSP` + `GWT`, `XUL`, `XAML`, `flex`, `boost`(C++)
* Tools: Git, 熟悉 Unix/Linux
* Objective: 能融入團隊，參與stable, large-scale, next-gen 專案的開發，並具備良好的書寫與口頭溝通能力。

---

## 後續工作
* 整合三家公司的 Job Description 資料進行分析，即可了解當前業界最普遍、常見的資訊人才需求。
* 最後根據可支配收入分析「出國找工作」真的賺比較多？還是待在國內其實比較好?
* 現實中，要進大公司非常困難，而不是像資料顯示的那麼簡單。想辦法解釋資料與現實的差距？
