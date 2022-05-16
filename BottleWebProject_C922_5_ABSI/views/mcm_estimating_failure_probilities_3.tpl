% rebase('layout.tpl', title='Estimating failure probilities 3 tread', year=year)

<!--Для вывода формул-->
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

<!--Заголовок страницы - верхушка-->
<div>
    <p><br></p>
    <!-- добавляем текст - заговок страницы-->
    <headerParagraphAbout class="A">Efficient Monte Carlo methods for estimating failure probabilities <br>3 thread<br></headerParagraphAbout>
    <!--Разделяем на абзацы-->
    <hr></hr>
</div>
<!--Блок для ввода и примера-->
<div>
    <headerA1>Your Task:</headerA1>
    <!--Разделяем на абзацы-->
    <hr></hr>
    <!--Изображене справа-->
    <div class="circular--portraitV"> <img src="static\images\mcm_estimating_failure_probilities_3\v1.png"/> </div>
    <!--Основной текст ждя задачи-->
    <pHP>A three thread queuing system for estimating failure probabilities. The time between the receipt of two consecutive applications is 
    distributed according to the exponential law:$${f(\tau) = \alpha*e^{-\alpha\tau}}$$ 
    The service duration of each application is equal to t1 min. Find by the Monte Carlo method 
    the mathematical expectation of the number of applications served during the time T = t2 hours.</pHP>
    <p><br></p>
    <!--Разделяем на абзацы-->
    <hr></hr>
    <headerA1>Enter your data:</headerA1>
    <!--Разделяем на абзацы-->
    <hr></hr>
    
    <form action="/mcm_estimating_failure_probilities_3" method="post">
   
    <p><br></p>
        <table class="tbV"><!--Таблица-->
            <tr><!--Шапка таблицы-->
                <th>t1</th>
                <th>t2</th>
                <th>$${\alpha}$$ </th>
            </tr>
            <tr><!--Ячейки для ввода -->
                <td><input type="number" step="0.01" size="5" min="0" name="NUMBER_t1" placeholder="0.5" required oninvalid="this.setCustomValidity('Enter the probability of the first element!')" oninput="this.setCustomValidity('')"></td>
                <td><input type="number" step="0.01" size="5" min="1" name="NUMBER_t2" placeholder="2" required oninvalid="this.setCustomValidity('Enter the probability of the second element!')" oninput="this.setCustomValidity('')"></td>
                <td><input type="number" step="0.01" size="5" min="0" name="NUMBER_a" placeholder="0.85" required oninvalid="this.setCustomValidity('Enter the probability of the third element!')" oninput="this.setCustomValidity('')"></td>
            </tr>
        </table>
        <br>
        <headerV1>
            Numer of tests: <!--Ячейка для ввода -->
            <input type="number" step="1" size="5" min="1" name="NUMBER_N" placeholder="5" required oninvalid="this.setCustomValidity('Enter the number of tests!')" oninput="this.setCustomValidity('')">
        </headerV1>
        <p><br></p>
        <p><input type="submit" class="buttonV" value="Calculate"></p>
        <p><br></p>
        <p><br></p>
    </form>
    <!--Разделяем на абзацы-->
    <hr class="about"></hr>
    <headerA1>Would you like to see an example? </headerA1>
    <hr></hr>
    <!--Изображение-->
    <div class="circular--portrait"> <img src="static\images\home\6.JPG"/></div>
     <!--Основной текст-->
    <pHP>A three thread queuing system for estimating failure probabilities. The time between the receipt of two consecutive applications is 
    distributed according to the exponential law:$${f(\tau) = 5*e^{-5\tau}}$$ 
    The service duration of each application is equal to 0.5 min. Find by the Monte Carlo method 
    the mathematical expectation of the number of applications served during the time T = 4 min.</p1>
    <hr></hr>
    <headerHP2>Solve<br></headerHP2><hr></hr>
    <pHP>If T1=0 is the moment of receipt of the first application. The application will be sent to the first channel and will be served by it. 
    The time of the end of the service of the first application: $${T_{1}+0.5=0+0.5=0.5}$$  In the counter of serviced applications, we write one.
    <br>The moments of receipt of subsequent applications will be found by the formula:$${T_{i}=T_{i-1}+\tau_{i}}$$where: $${\tau_{i}} $$
    - time between two consecutive applications with numbers i-1 and i.Possible: $${\tau_{i}=\frac{-1}{\lambda}*lnr_{i}}$$ By condition:
    $${\tau_{i}=-0.2*lnr_{i}}$$ We generate random numbers using a random number generator. Let the time between the receipt of the first and 
    second applications be a random number. Then:$${\tau_{2}=-0.2*ln(0.1)=0+0.460=0.46}$$The first application was received at the moment T1=0. 
    Therefore, the second application was received at the moment: $${T_{2}=T_{1}+0.460=0+0.460=0.460}$$ At this moment, the first channel is still 
    busy servicing the first application, so the second application will arrive in the second and will be serviced by it. The end of the service of the 
    second application is T2+0.5=0.460+0.5=0.960. We add one to the counter of served requests, that why:$${T_{2}+0.5 =0.460+0.5=0.960}$$
    The second random number is 0.09, we go similarly to the second example. By click you can watch a table with a detailed solution.<br><br>
    <a class="buttonV" href="#popup1">Table</a><br><br>From the table we find that in 4 minutes a total of 20 applications were received; 
    x1 = 12 were served. Let's perform five more tests in the same way, we get: x2 = 15, x3 = 14, x4 = 12, x5 = 13, x6 = 15.As an estimate 
    of the desired mathematical expectation a - the number of applications served, we will take a sample average:
    $${a=\bar{(x)}=\frac{2*12+13+14+2*15}{6}=13.5}$$
    </pHP>

</div>
<!--Разделяем на абзацы-->
<hr class="about">
</hr>
<!--Первое сплывающее окно-->
<div id="popup1" class="overlay">
	<div class="popup">
        <!--заговок окна-->
		<h1>Table</h1>
        <hr></hr>
		<a class="close" href="#">x</a>
		<div class="content">
            <!--Изображение текста-->
           <div class="circular--portraitV2"> <img src="static\images\mcm_estimating_failure_probilities_3\v3.png" /></div>
		</div>
	</div>
</div>
