% rebase('layout.tpl', title='Simulation Modeling', year=year)
  <p><br></p>
  <p><br></p>
<form action="/mcm_system_reliability_2_3" method="post">

        <!-- добавл€ем текстовое поле дл€ почты, использу€ паттерн-->
        <p><input type="number" step="0.01" size="50" name="A" placeholder="A" min="0" max="1" required oninvalid="this.setcustomvalidity('enter first parameters!')" 
        oninput="this.setcustomvalidity('')"></p>

        <!-- добавл€ем текстовое поле дл€ почты, использу€ паттерн-->
        <p><input type="number" step="0.01" size="50" name="B" placeholder="B" min="0" max="1" required oninvalid="this.setcustomvalidity('enter second parameters!')" 
        oninput="this.setcustomvalidity('')"></p>

        <!-- добавл€ем текстовое поле дл€ почты, использу€ паттерн-->
        <p><input type="number" step="0.01" size="50"  name="C" placeholder="C" min="0" max="1" required oninvalid="this.setcustomvalidity('enter third parameters!')" 
        oninput="this.setcustomvalidity('')"></p>

        <!-- добавл€ем текстовое поле дл€ почты, использу€ паттерн-->
        <p><input type="number"  step="0.01" size="50" name="D" placeholder="D" min="0" max="1" required oninvalid="this.setcustomvalidity('enter fourth parameters!')" 
        oninput="this.setcustomvalidity('')"></p>
        
        <p><input type="number"  step="0.01" size="50" name="E" min="0" max="1" placeholder="E" required oninvalid="this.setcustomvalidity('enter fourth parameters!')" 
        oninput="this.setcustomvalidity('')"></p>

        <!-- кнопка дл€ отправки-->
        <p><input type="submit"  class="buttonHP" value="send"></p>

</form>

