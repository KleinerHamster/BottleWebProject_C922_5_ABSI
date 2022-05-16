%rebase('layout.tpl', title='Estimating failure probilities', year=2022)

<!--Для вывода формул-->
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>


<!--Заголовок страницы - верхушка-->
<div>
	<p><br></p>
	<!-- добавляем текст - заговок страницы-->
	<headerParagraphAbout class="A">Efficient Monte Carlo methods for estimating failure probabilities <br>{{number_mcm}} thread<br></headerParagraphAbout>
	<!--Разделяем на абзацы-->
    <hr></hr>
</div>

<!--Основной блок-->
<div>
	<pHP>
	<!--Изображение-->
	<div class="circular--portraitV1"> <img src="static\images\mcm_estimating_failure_probilities_3\v4.png"/> </div>
	<!--Основной текст-->
	From the table we find that in {{time}} min a total of {{total_count}} applications were received; x1 = {{number_of_requests_served}} were served. Let's perform 
	{{all_tests}} more tests in the same way, we get:<br>{{!html1}}<br><!--Таблица результатов теста-->
	As an estimate of the desired mathematical expectation a - the number of applications served , we will take a sample average:
	$${a=\bar{(x)}=\frac{\sum{x_{i}}}{n}}={{result}}$$<br><br>
	<!--Разделяем на абзацы-->
    <hr></hr>
	<headerA1>Would you like to back? <a class="buttonV1" href={{button_back}}>Back</a></headerA1><br><br>
	<!--Разделяем на абзацы-->
    <hr></hr>
	</pHP>
</div>

<!--Таблица с первого теста-->
{{!html}}


<!--Разделяем на абзацы-->
<p><br></p>
<hr class="about"></hr>
