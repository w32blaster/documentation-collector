<#assign content = {"rootpath" : "../"}>

<#include "header.ftl">
	
<#include "menu.ftl">

<div class="container-fluid">

      <div class="row">

            <div class="col-md-3">
            	 <#include "toc.ftl">
            </div>
            <div class="col-md-9">
            
                  <div class="page-header">
				<h2>Tag: <span class="label label-info"> <span class="glyphicon glyphicon-tag" aria-hidden="true"></span> ${tag}</span> </h2>
			</div>
			
			<ul>
				<#list tag_posts as post>
				<#if (last_month)??>
					<#if post.date?string("MMMM yyyy") != last_month>
						</ul>
						<h4>${post.date?string("MMMM yyyy")}</h4>
						<ul>
					</#if>
				<#else>
					<h4>${post.date?string("MMMM yyyy")}</h4>
					<ul>
				</#if>
				
				<li>${post.date?string("dd")} - <a href="<#if (content.rootpath)??>${content.rootpath}<#else></#if>${post.uri}">${post.title}</a></li>
				<#assign last_month = post.date?string("MMMM yyyy")>
				</#list>
			</ul>
                  
            </div>
      </div>
</div>


<#include "footer.ftl">