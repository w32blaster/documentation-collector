<#include "header.ftl">

<#include "menu.ftl">

<div class="container-fluid">
	<div class="row">	

	      <div class="col-md-3"> 
	      		<#include "toc.ftl"> 
	      </div>
	      <div class="col-md-9">

			<p><em>${content.date?string("dd MMMM yyyy")}</em></p>
			
			Tags: 
			<#list content.tags as k>
				<a href="<#if (content.rootpath)??>${content.rootpath}<#else></#if>tags/${k}.html">
					<span class="label label-info">
						<span class="glyphicon glyphicon-tag" aria-hidden="true"></span> ${k}  
					</span>
				</a>
				&nbsp;
			</#list>


			<div class="page-header">
				<h1><#escape x as x?xml>${content.title}</#escape></h1>
			</div>

			<table>
				<tr>
					<td>Author</td>
					<td> ${(content.author)!"unknown"} </td>
				</tr>	
				<tr>
					<td>Jira Issue</td>
					<td>
						<#if (content.jira)??>
							<a href="${content.jira}">
								<#assign urlParts = content.jira?split("/") >
								${urlParts[urlParts?size-1]}
							</a>
						<#else>
							<p class="text-muted">not set</p>
						</#if>
					</td>
				</tr>
				<tr>
					<td>Docker</td>
					<td> ${(content.docker)!'<p class="text-muted">not set</p>'} </td>
				</tr>
			</table>


			<p>${content.body}</p>

		</div>
	</div>	
</div>

<#include "footer.ftl">