<!--
      The Table of contents
-->
<ul class="nav nav-pills nav-stacked">
<#list posts?sort_by("title") as post>
            <#if (post.status == "published")>
                  <#if content.sha1??>
                        <#if (post.sha1 == content.sha1)>
                              <!-- active link -->
                              <li class='active'>
                                    <a href="#">
                                          <#escape x as x?xml>${post.title}</#escape> 
                                    </a>
                              </li>
                        <#else>
                              <li>
                                    <a href="<#if (content.rootpath)??>${content.rootpath}<#else></#if>${post.uri}">
                                          <#escape x as x?xml>${post.title}</#escape> 
                                    </a>
                              </li>
                        </#if>
                  <#else>
                        <li>
                              <a href="<#if (content.rootpath)??>${content.rootpath}<#else></#if>${post.uri}">
                                    <#escape x as x?xml>${post.title}</#escape> 
                              </a>
                        </li>
                  </#if>
                  
            </#if> 
      </li>
</#list>
</ul>


      