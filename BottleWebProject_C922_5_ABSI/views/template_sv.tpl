%rebase('layout.tpl', title='Estimating failure probilities', year=2022)

<!--��� ������ ������-->
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>


<!--��������� �������� - ��������-->
<div>
	<p><br></p>
	<!-- ��������� ����� - ������� ��������-->
	<headerParagraphAbout class="A">Efficient Monte Carlo methods for estimating failure probabilities <br>{{number_mcm}} thread<br></headerParagraphAbout>
	<!--��������� �� ������-->
    <hr></hr>
</div>

<!--�������� ����-->
<div>
	<pHP>
	<!--�����������-->
	<div class="circular--portraitV1"> <img src="static\images\mcm_estimating_failure_probilities_3\v4.png"/> </div>
	<!--�������� �����-->
	From the table we find that in {{time}} min a total of {{total_count}} applications were received; x1 = {{number_of_requests_served}} were served. Let's perform 
	{{all_tests}} more tests in the same way, we get:<br>{{!html1}}<br><!--������� ����������� �����-->
	As an estimate of the desired mathematical expectation a - the number of applications served , we will take a sample average:
	$${a=\bar{(x)}=\frac{\sum{x_{i}}}{n}}={{result}}$$<br><br>
	<!--��������� �� ������-->
    <hr></hr>
	<headerA1>Would you like to back? <a class="buttonV1" href={{button_back}}>Back</a></headerA1><br><br>
	<!--��������� �� ������-->
    <hr></hr>
	</pHP>
</div>

<!--������� � ������� �����-->
{{!html}}


<!--��������� �� ������-->
<p><br></p>
<hr class="about"></hr>
