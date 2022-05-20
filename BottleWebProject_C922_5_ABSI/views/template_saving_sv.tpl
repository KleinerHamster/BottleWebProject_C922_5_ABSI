<br><img src="static\images\home\logo.png" alt="logo" style="width:80px;height:28px;">

<!--Для вывода формул-->
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>


<!--Заголовок страницы - верхушка-->
<div>
	<!-- добавляем текст - заговок страницы-->
	<headerParagraphAbout class="A">Efficient Monte Carlo methods for estimating failure probabilities {{number_mcm}} thread<br></headerParagraphAbout>
	<!--Разделяем на абзацы-->
    <hr></hr>
</div>

<!--Количество проведенных тестов-->
<headerMCM32>Number of tests: {{N}}</headerMCM32>
<table class="tbV"><!--Таблица -->

    <caption><headerA1>Probabilities of elements:</headerA1></caption>
    <tr><!--Шапка таблицы-->
        <th>t1</th>
        <th>t2</th>
        <th>a</th>
    </tr>
    <tr><!--Ячейки для ввода -->
        <td>{{t1}}</td>
        <td>{{t2}}</td>
        <td>{{a}}</td>
    </tr>
</table>

<hr></hr>

<!--Основной блок-->
<div>
	<pHP>
	<!--Основной текст-->
	From the table we find that in {{time}} min a total of {{total_count}} applications were received; x1 = {{number_of_requests_served}} was served (or is being served). Let's perform 
	{{all_tests}} more tests in the same way, we get:<br>{{!html1}}<br><!--Таблица результатов теста-->
	As an estimate of the desired mathematical expectation a - the number of applications served , we will take a sample average:
	$${a=\bar{(x)}=\frac{\sum{x_{i}}}{n}}={{result}}$$
	<!--Разделяем на абзацы-->
    <hr></hr>
	Table from the first test:
	</pHP>
</div>
<!--Таблица с первого теста-->
{{!html}}


%import datetime
%today = datetime.datetime.today()
%printToday = today.strftime("%H:%M:%S %d.%m.%Y")

<!--Разделяем на абзацы-->
<hr class="about"></hr>
<div class="container body-content">
    <footer>
        <pEnd>&copy; {{printToday}} - KVAS Corporation</pEnd>
    </footer>
</div>