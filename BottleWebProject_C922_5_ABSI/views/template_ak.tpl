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
    <caption><headerA1>Probabilities of elements:</headerA1></caption>
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



<hr></hr>

<table class="tbV"><!--Таблица-->
    <caption><headerA1>Probability of uptime:</headerA1></caption>
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

<headerA1>Test results:</headerA1>

<!--Таблица с первого теста-->
{{!html}}

<!--Разделяем на абзацы-->
<p><br></p>
<hr class="about"></hr>
