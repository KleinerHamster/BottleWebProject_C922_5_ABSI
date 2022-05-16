%rebase('layout.tpl', title='mcm_system_reliability', year=2022)
<!--Заголовок страницы - верхушка-->
<div>
    <p><br></p>
    <!-- добавляем текст - заговок страницы-->
    <headerParagraphAbout class="A">Evaluation of the reliability of the simplest systems by the Monte Carlo method<br></headerParagraphAbout>
    <!--Разделяем на абзацы-->
    <hr >
    </hr>
</div>

<table class="tbV"><!--Таблица-->
    <caption><headerHP2>Probabilities of elements:</headerHP2></caption>
    <tr><!--Шапка таблицы-->
        <th>A</th>
        <th>B</th>
        <th>C</th>
        <th>D</th>
        <th>E</th>
    </tr>
    <tr><!--Ячейки для ввода -->
        <td>{{A_str}}</td>
        <td>{{B_str}}</td>
        <td>{{C_str}}</td>
        <td>{{D_str}}</td>
        <td>{{E_str}}</td>
    </tr>
</table>

<headerHP2>Number of tests: {{N_str}}</headerHP2>

<hr></hr>

<table class="tbV"><!--Таблица-->
    <caption><headerHP2>Probability of uptime:</headerHP2></caption>
    <tr><!--Шапка таблицы-->
        <th>P*</th>
        <th>P1</th>
        <th>P2</th>
        <th>P</th>
        <th>P-P*</th>
    </tr>
    <tr><!--Ячейки для ввода -->
        <td>{{A_str}}</td>
        <td>{{B_str}}</td>
        <td>{{C_str}}</td>
        <td>{{D_str}}</td>
        <td>{{E_str}}</td>
    </tr>
</table>

<hr></hr>

<headerHP2>Test results:</headerHP2>

<!--Таблица с первого теста-->
{{!html}}

<!--Разделяем на абзацы-->
<p><br></p>
<hr class="about"></hr>
