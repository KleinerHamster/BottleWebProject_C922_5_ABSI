% rebase('layout.tpl', title='Simulation Modeling', year=year)
  <p><br></p>
  <p><br></p>
  <!--«аголовок страницы - верхушка-->
<div>
    <p><br></p>
    <!-- добавл€ем текст - заговок страницы-->
    <headerParagraphAbout class="A">Evaluation of the reliability of the simplest systems by the Monte Carlo method<br></headerParagraphAbout>
    <!--–аздел€ем на абзацы-->
    <hr >
    </hr>
</div>
<div>
      <headerA1>Theoretical information </headerA1>
      <hr></hr>
      <pHP>Simulation modeling is obtaining experimental information about a complex object, which cannot be obtained in any other way except by experimenting with its model on a computer.
        The Monte Carlo method is a statistical modeling or simulation method. This is a numerical method for solving problems by modeling random variables.
        The idea of the method is extremely simple and consists in the following.
        Instead of describing the process with the help of an analytical apparatus, a drawing of a random phenomenon is carried out using a specially organized procedure that includes randomness and gives a random result. The implementation of a random process develops differently each time, i.e. we get different outcomes of the process under consideration. This set of implementations can be used as some kind of artificially obtained statistical material that can be processed by conventional methods of mathematical statistics. After such processing, you can get: the probability of an event, mathematical expectation, etc.
        Using the Monte Carlo method, any probabilistic problem can be solved, but it is justified when the drawing procedure is simpler, and not more complicated than analytical calculation.</pHP>
      <hr></hr>
</div>
<div>
      <headerA1>Task description </headerA1>
      <hr></hr>
      <pHP>The system consists of two blocks connected in series. The system fails when at least one block fails. The first block contains two elements: A, B, and the second contains three elements: C, D, E. The elements of each block are connected in parallel. The block fails when all the elements included in it fail at the same time. The probability of failure-free operation of elements P(A), P(B), P(C), P(D), P(E) is entered by the user.
After 100 tests, the Monte Carlo method is used to find an estimate of the P * reliability of the system. Find the absolute error P*-P, where P is the reliability of the system, calculated analytically.</pHP>
      <hr></hr>
</div>

<form action="/mcm_system_reliability_2_3" method="post">

        <!-- добавл€ем текстовое поле дл€ почты, использу€ паттерн-->
        <p><input type="number" step="0.01" size="50" name="A" placeholder="A" min="0" max="1" required oninvalid="this.setcustomvalidity('enter first parameters two decimal places!')" 
        oninput="this.setcustomvalidity('')"></p>

        <!-- добавл€ем текстовое поле дл€ почты, использу€ паттерн-->
        <p><input type="number" step="0.01" size="50" name="B" placeholder="B" min="0" max="1" required oninvalid="this.setcustomvalidity('enter second parameters two decimal places!')" 
        oninput="this.setcustomvalidity('')"></p>

        <!-- добавл€ем текстовое поле дл€ почты, использу€ паттерн-->
        <p><input type="number" step="0.01" size="50"  name="C" placeholder="C" min="0" max="1" required oninvalid="this.setcustomvalidity('enter third parameters two decimal places!')" 
        oninput="this.setcustomvalidity('')"></p>

        <!-- добавл€ем текстовое поле дл€ почты, использу€ паттерн-->
        <p><input type="number"  step="0.01" size="50" name="D" placeholder="D" min="0" max="1" required oninvalid="this.setcustomvalidity('enter fourth parameters two decimal places!')" 
        oninput="this.setcustomvalidity('')"></p>
        
        <p><input type="number"  step="0.01" size="50" name="E" min="0" max="1" placeholder="E" required oninvalid="this.setcustomvalidity('enter fourth parameters two decimal places!')" 
        oninput="this.setcustomvalidity('')"></p>

        <!-- кнопка дл€ отправки-->
        <p><input type="submit"  class="buttonHP" value="send"></p>

</form>

