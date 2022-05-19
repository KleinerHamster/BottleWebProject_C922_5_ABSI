% rebase('layout.tpl', title='Home Page', year=year)
<!--Для вывода формул-->
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Заголовок страницы - верхушка-->
<div>
    <p></p>
    <headerParagraphAbout class="A">Simulation modeling. Queuing systems.</headerParagraphAbout>
    <headerParagraphAbout class="A">Monte Carlo method for finding the mathematical expectation</headerParagraphAbout>
    <!--Разделяем на абзацы-->
    <hr></hr>
</div>
<!--Блок задания-->
<div>
    <headerA1>Task:</headerA1>
    <!--Основной текст для задачи (формулировка задачи)-->
    <pHP>A four thread queuing system for estimating failure probabilities. The time between the receipt of two consecutive applications is 
    distributed according to the exponential law:$${f(\tau) = \alpha*e^{-\alpha\tau}}$$ 
    The service duration of each application is equal to t1 min. Find by the Monte Carlo method 
    the mathematical expectation of the number of applications served during the time T = t2 min.</pHP>
    <!--Следующая строка-->
    <p><br></p>
    <!--Разделяем на абзацы-->
    <hr></hr>
 </div>

<form action="/mcm_estimating_failure_probilities_4" method="post">
        <!--Изображене слева-->
        <div class="circular--portraitA"> <img src="static\images\mcm_estimating_failure_probilities_4\s1.png"/> </div>
        <br><headerA1>Input:<br>
        <!-- добавляем поле для ввода параметра t1 (длительность обслуживания каждой заявки), используя паттерн--> 
        t1: <input title ="t1"  class="V" type="number" min=0 step="0.01" size="50" id="t1" name="t1" placeholder="10, 0.32" required oninvalid="this.setCustomValidity('Enter first parameters two decimal places!')" 
        oninput="this.setCustomValidity('')"> <br><br>

        <!-- добавляем поле для ввода параметра t2 (за какое время будет обслужены заявки), используя паттерн-->
         t2: <input title ="t2" class="V" type="number" min=0 step="0.01" size="50" id="t2" name="t2" placeholder="12, 0.2" required oninvalid="this.setCustomValidity('Enter second parameters two decimal places!')" 
        oninput="this.setCustomValidity('')"><br><br>

        <!-- добавляем поле для ввода араметра a (параметр распределения показательного закона), используя паттерн-->
        a : <input title ="a" class="V" type="number" min=0.01 step="0.01" size="50" id="a" name="a" placeholder="23, 0.43" required oninvalid="this.setCustomValidity('Enter third parameters two decimal places!')" 
        oninput="this.setCustomValidity('')"> <br><br>

        <!-- добавляем поле для ввода параметра n (количество проведенных испытаний), используя паттерн-->
         n : <input title ="Count of tests" class="V" type="number" min=1 size="50" id="n" name="n" placeholder="1" required oninvalid="this.setCustomValidity('Enter fourth parameters two decimal places!')" 
        oninput="this.setCustomValidity('')"><br><br>

        <!-- кнопка для отправки-->
        <input class="buttonS" type="submit"  class="btn btn-default" value="Send">
        <br><br>
        </headerA1>
</form>

<hr class="about">

<!--Описание примера-->
<headerA1>Example<br></headerA1>
<pHP>Task conditions:
    <br>
    A four-channel queuing system with failures receives a Poisson flow of applications. 
    The time between the receipt of two consecutive applications is distributed according to 
    the exponential law: $${f(\tau) = 5*e^{-5\tau}}$$ The service duration of each application is 0.5 minutes. 
    Find by the Monte Carlo method the mathematical expectation a of the number of applications 
    served during the time T = 4 min.<br><hr></hr>
   <headerA1>Solving<br></headerA1>
   Let T1=0 be the moment of receipt of the first application. The application will be sent to 
   the first channel and will be served by it. The time of the end of the service of the first application:$${T_{1}+0.5=0+0.5=0.5}$$
   In the counter of serviced applications, we write one.
   <br>The moments of receipt of subsequent applications will be found by the formula:$${T_{i}=T_{i-1}+\tau_{i}}$$
   where $${\tau_{i}} $$ - the length of time between two consecutive applications with numbers i-1 and i.
   <br>Possible: $${\tau_{i}=\frac{-1}{\lambda}*lnr_{i}}$$
   <br>Given that, by the condition:$${\lambda=5}$$ we get  $${\tau_{i}=-0.2*lnr_{i}}$$
   Random numbers ri are generated using a random number generator. Let the time between the receipt of the 
   first and second applications be a random number equal to r1 = 0.10.
   <br>Then: $${\tau_{2}=-0.2*ln(0.1)=0+0.460=0.46}$$ The first application was received at the moment T1=0. Therefore, 
   the second application was received at the moment $${T_{2}=T_{1}+0.460=0+0.460=0.460}$$ At this moment, 
   the first channel is still busy servicing the first application, so the second application will 
   arrive in the second and will be serviced by it. 
   <br>The end of the service of the second application is T2+0.5=0.460+0.5=0.960. We add one to the counter of served requests. 
   <br>According to the next random number r2=0.09, we will play the time TAU3 between the receipt of the second and third applications:
   $${T_{3}=-0.2*ln(0.09)=0.2*2.41=0.482}$$
   The second application was received at the time T2= 0.460. 
   Therefore, the third application was received at the moment  $${T_{3}=T_{2}+0.482=0.460+0.482=0.942}$$
   At this moment, the first channel is already free, and the third application will be received
   in the first channel. The end of the service of the third application is T3+0.5=0.942+0.5=1.442. 
   We add one to the counter of served requests. Further calculation is performed similarly (Table 1), 
   moreover, if at the time of receipt of the application all channels are busy (the time of receipt of 
   the application is less than each of the moments of the end of service), then one is added to the failure counter.
   <br>Note that the service of the 20th application will end at the moment 4.148>4, so this application is rejected.
   <br>The test is terminated ("stop" is recorded in the table) if the time of receipt of the application is T>4.<br>
   Table 1<br>
</pHP>
<!--Вставка таблица из oneDrive-->
<iframe class="S" src="https://onedrive.live.com/embed?resid=64BE450E1A82AA1A%217489&authkey=%21AOjobiUA_xsLwPU&em=2&wdAllowInteractivity=False&wdHideGridlines=True&wdHideHeaders=True&wdDownloadButton=True&wdInConfigurator=True&wdInConfigurator=True&edesNext=false&ejss=false"></iframe>

<pHP>
<br>From the table we find that in 4 minutes a total of 20 applications were received; x1 = 17 were served. 
<br>Let's perform five more tests in the same way, we get: x2=15, x3=14, x4=17, x5 =13, x6=15.
<br>As an estimate of the desired mathematical expectation a - the number of applications served, we will take a sample average:
$${a=\bar{(x)}=\frac{2*17+2*15+14+13}{6}=15.2}$$
result: a=15.2
</pHP>