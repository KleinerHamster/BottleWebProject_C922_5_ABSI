% rebase('layout.tpl', title='Simulation Modeling', year=year)
<!--Для вывода формул-->
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <p><br></p>
  <!--Заголовок страницы - верхушка-->
<div>
    <p><br></p>
    <!-- добавляем текст - заговок страницы-->
    <headerParagraphAbout class="A">Evaluation of the reliability of the simplest systems by the Monte Carlo method<br></headerParagraphAbout>
    <!--Разделяем на абзацы-->
    <hr >
    </hr>
</div>
<div>
<div>
      <headerA1>Task description </headerA1>
      <hr></hr>
      <pHP>The system consists of two blocks connected in series. The system fails when at least one block fails. The first block contains two elements: A, B, and the second contains three elements: C, D, E. The elements of each block are connected in parallel. The block fails when all the elements included in it fail at the same time. The probability of failure-free operation of elements P(A), P(B), P(C), P(D), P(E) is entered by the user.
After 100 tests, the Monte Carlo method is used to find an estimate of the P * reliability of the system. Find the absolute error P*-P, where P is the reliability of the system, calculated analytically.</pHP>
      <hr></hr>
</div>

<form action="/mcm_system_reliability_2_3" method="post">
        <!--Изображене слева-->
        <div class="circular--portraitK"> <img src="static\images\mcm_system_reliability_2_3\k1.png"/> </div>
        <br><headerA1>Enter your data:<br>

        <!-- добавляем текстовое поле для первого блока, используя паттерн-->
        <input  title="Block A" type="number" class="K" step="0.01" size="10" name="A" placeholder="P(A)" min="0" max="1" required oninvalid="this.setCustomValidity('Enter the first parameter two decimal places of!')" 
        oninput="this.setCustomValidity('')"> 

        <!-- добавляем текстовое поле для 2-ого блока, используя паттерн-->
        <input title="Block B" type="number" class="K" step="0.01" size="10" name="B" placeholder="P(B)" min="0" max="1" required oninvalid="this.setCustomValidity('Enter the second parameters two decimal places!')" 
        oninput="this.setCustomValidity('')"><br><br>

        <!-- добавляем текстовое поле для 3-го блока, используя паттерн-->
        <input title="Block C" type="number" class="K" step="0.01" size="10"  name="C" placeholder="P(C)" min="0" max="1" required oninvalid="this.setCustomValidity('Enter the third parameters two decimal places!')" 
        oninput="this.setCustomValidity('')"> 

        <!-- добавляем текстовое поле для 4-го блока, используя паттерн-->
        <input title="Block D" type="number" class="K" step="0.01" size="10" name="D" placeholder="P(D)" min="0" max="1" required oninvalid="this.setCustomValidity('Enter the fourth parameters two decimal places!')" 
        oninput="this.setCustomValidity('')"><br><br>

         <!-- добавляем текстовое поле для 5-го блока, используя паттерн-->
        <input title="Block E" type="number" class="K" step="0.01" size="10" name="E" min="0" max="1" placeholder="P(E)" required oninvalid="this.setCustomValidity('Enter the fifth parameters two decimal places!')" 
        oninput="this.setCustomValidity('')">

        <!-- добавляем текстовое поле для кол-ва тествов, используя паттерн-->
        <input title="Number of test" type="number" class="K" step="1" size="10" name="n" min="1" placeholder="n" required oninvalid="this.setCustomValidity('Enter number of tests!')" 
        oninput="this.setCustomValidity('')"><br><br>

        <!-- кнопка для отправки-->
        <p><input type="submit" class="buttonS" value="send"></p>
        <br><br>
        </headerA1>

</form>
<!--Разделяем на абзацы-->
<hr class="about"></hr>

<!--Блок с примером-->
<div>
    <headerA1>Example<br></headerA1>
    <pHP>Task conditions:<br>
    <!--Основной текст-->
    The system consists of two blocks connected in series. The system fails when at least one block fails. The first block contains three elements: A, B, C 
    (they are connected in parallel) and fails when three elements fail simultaneously. The second one contains two elements D, E and fails when two elements fail 
    simultaneously.<br>a) Find by the Monte Carlo method an estimate of P* reliability (probability of failure-free operation) of the system, knowing the probability 
    of failure-free operation of the elements: P(A) = 0.8, P(B)=0.9, P(C)=0.85, P(D)=0.85, P(E)=0.85;<br>b) find the absolute error: $${|P - P*|}$$
    of the found value, where P is the reliability of the system, calculated analytically.<br>Perform 100 tests.</pHP>
    <!--Разделяем на абзацы-->
    <hr></hr>
    <headerA1>Solving<br></headerA1>
    <!--Основной текст-->
    <pHP>
    a) Using a random number generator, we obtain (or select from special tables of uniformly distributed random numbers) 5 random numbers, 
    for example: 0.97, 0.12, 0.48, 0.22, 0,64; next, we consider that if the random number is less than the probability of the corresponding event, then the event 
    has occurred (the element works flawlessly); if the random number is greater than or equal to the probability of the event, then the event has not occurred (failure).
    <br>We will play the events A, B, C, D, E consisting in the trouble-free operation of the ABC, D, E elements, respectively. We will record the test results in the 
    calculation table. Since P(A) = 0.8 and 0.10 < 0.8, this event did not occur, i.e. element A in this test works with failure. Since P(B) = 0.9 and 0.12 < 0.9, 
    this event B has occurred, i.e. element B works flawlessly, etc.<br>Thus, two of the three elements of the first block work; therefore, the first block itself works. 
    In the corresponding cells of Table, we put a plus sign.<br>If all the events in the block did not occur, i.e. the elements were rejected; in other words, the block,
    and therefore the entire system, are rejected. In the corresponding cells of Table 1, we put a minus sign.<br>The other tests are played out in the same way. The 
    Table shows the results of one hundred tests.
    By click you can watch a example table with a detailed solution for 7 tests.<br><br><a class="buttonV" href="#popup1">Table</a><br><br>
    After making 100 tests, we get that in 95 of them the system worked flawlessly. As an estimate of the desired reliability P, we take the relative frequency:
    $$P* = {95\over100}= 0.95 $$<br>b) Find the reliability of the system P analytically. The probabilities of failure-free operation of the first and second blocks are equal, 
    respectively:<br>$${P_{1} = 1 - P\bar{(A)} * P\bar{(B)}=1-(1-0.8)*(1-0.9)*(1-0.85)=0.997}$$ 
    <br>$${P_{2} = 1 - P\bar{(C)} * P\bar{(D)}=1-(1-0.7)*(1-0.78)=0.934}$$ 
    <br>Probability of system uptime:
    <br>$${P = P1*P2=0.997*0.934=0.931}$$<br>The required absolute error is equal to:<br>$${|P - P*| = |0.931-0.95|=|-0.019|=0.019}$$
    </pHP>
</div>

<!--Разделяем на абзацы-->
<hr class="about"></hr>

<!--Первое сплывающее окно-->
<div id="popup1" class="overlay">
	<div class="popup">
        <!--заговок окна-->
		<h1>Table</h1>
        <hr></hr>
		<a class="close" href="#">x</a>
		<div class="content">           
            <!--Контейнер-->
            <conteinerForText>
                <!--делим на три колонки наш блок-->
                <!--пустая колонка-->
                <delimeterPerson>
                </delimeterPerson>
                <delimeterPerson>
                </delimeterPerson>
                <separateForText>
                     <!--Изображение текста-->
                     <div class="circular--portraitK1"> <img src="static\images\mcm_system_reliability_2_3\k2.png" /></div>
                 </separateForText>
                <!--пустая колонка-->
                <delimeterPerson>
                </delimeterPerson>
            </conteinerForText>
		</div>
	</div>
</div>
