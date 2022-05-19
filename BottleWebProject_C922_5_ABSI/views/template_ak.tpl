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
<!--Количество проведенных тестов-->
<headerMCM32>Number of tests: {{N_str}}</headerMCM32>
<table class="tbV"><!--Таблица -->

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
        <th>|P-P*|</th>
    </tr>
    <tr><!--Ячейки для ввода -->
        <td>{{p_star}}</td>
        <td>{{round(p1, 3)}}</td>
        <td>{{round(p2, 3)}}</td>
        <td>{{round(p, 3)}}</td>
        <td>{{round(p_pStar,3)}}</td>
    </tr>
</table>

<!--Разделяем на абзацы-->
    <hr></hr>
	<headerA1>Would you like to back? <a class="buttonV1" href={{button_back}}>Back</a></headerA1><br><br>
	<!--Разделяем на абзацы-->
    <hr></hr>


<headerMCM32>Test results:</headerMCM32>

<!--Таблица с первого теста-->
{{!html}}

<!--Разделяем на абзацы-->
<p><br></p>
<hr class="about"></hr>
