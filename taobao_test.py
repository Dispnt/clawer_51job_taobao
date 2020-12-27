import base64
from bs4 import BeautifulSoup

# def b64_for_account_info(info):
#     info = info.encode()
#     res = base64.b64encode(info).decode()
#     return res
#
# def decode_test(info):
#     info = info.encode()
#     res = base64.b64decode(info).decode()
#     return res
#
# print(b64_for_account_info(''))
# print(decode_test(b64_for_account_info('')))

# page = '1/3'
# print(page.split('/')[1])
html = '''
<div class="m-sortbar" id="J_relative">
  <div class="sort-row">
    <div class="sort-inner">
      <ul class="sorts">
  
    
      <li class="sort">
        <a class="J_Ajax link active first" data-url="sortbar" data-key="sort" data-value="default" data-anchor="J_relative" trace="sortDefault" title="综合排序" href="#">综合排序</a>
      </li>
    
  
    
      <li class="sort">
        <a class="J_Ajax link  " data-url="sortbar" data-key="sort" data-value="sale-desc" data-anchor="J_relative" trace="sortSaleDesc" title="销量从高到低" href="#">销量</a>
      </li>
    
  
    
      <li class="sort">
        <a class="J_Ajax link  " data-url="sortbar" data-key="sort" data-value="credit-desc" data-anchor="J_relative" trace="sortCreditDesc" title="信用从高到低" href="#">信用</a>
      </li>
    
  
    
      <li class="sort has-droplist J_LaterHover" data-hover-cls="has-droplist-hover" tabindex="0">
        <div class="trigger">
          <div class="link  ">
            <span class="text" title="价格从低到高">价格</span>
            <span class="icon icon-btn-arrow-2-h"></span>
          </div>
        </div>

        <ul class="droplist">
          
            <li class="sort">
            <a class="J_Ajax link" tabindex="0" data-url="sortbar" data-key="sort" data-value="price-asc" data-anchor="J_relative" trace="sortPrice" href="#">价格从低到高</a>
            </li>
          
            <li class="sort">
            <a class="J_Ajax link" tabindex="0" data-url="sortbar" data-key="sort" data-value="price-desc" data-anchor="J_relative" trace="sortPrice" href="#">价格从高到低</a>
            </li>
          
            <li class="sort">
            <a class="J_Ajax link" tabindex="0" data-url="sortbar" data-key="sort" data-value="total-asc" data-anchor="J_relative" trace="sortPrice" href="#">总价从低到高</a>
            </li>
          
            <li class="sort">
            <a class="J_Ajax link" tabindex="0" data-url="sortbar" data-key="sort" data-value="total-desc" data-anchor="J_relative" trace="sortPrice" href="#">总价从高到低</a>
            </li>
          
        </ul>
      </li>
    
  
</ul>



      
        <div class="prices">
  <div class="inputs J_LaterHover" data-hover-cls="inputs-hover">
    <div class="inner">
      <ul class="items g-clearfix">
        <li class="item">
          <input class="J_SortbarPriceInput input" placeholder="¥" type="text" value="" aria-label="价格最小值">
        </li>
        <li class="sep">-</li>
        <li class="item">
          <input class="J_SortbarPriceInput input" placeholder="¥" type="text" value="" aria-label="价格最大值">
        </li>
        <li class="submit">
          <button class="J_SortbarPriceSubmit btn" type="button">确定</button>
        </li>
      </ul>
    </div>
  </div>

  

</div>

      

      
        <div class="pager">
  <ul class="items">
    
      <li class="item">
        <a class="link">
          <span class="icon icon-btn-prev-2-disable"></span>
        </a>
      </li>
    
    <li class="item" data-spm-anchor-id="a230r.1.0.i1.48881bcf6Z4Tv6"><span class="current" data-spm-anchor-id="a230r.1.0.i0.48881bcf6Z4Tv6">1</span>/3</li>
      
        <li class="item">
          <a class="J_Ajax J_Pager link icon-tag" href="#" title="下一页" trace="srp_select_pagedown" data-url="pager" data-key="s" data-value="44">
            <span class="icon icon-btn-next-2"></span>
          </a>
        </li>
      
  </ul>
</div>

      


      
        <div class="styles">
  <ul class="items">
    <li class="item">
      <a href="#" class="J_Ajax J_SortbarStyle link icon-tag active icon-hover" data-url="default" data-key="style" data-value="grid" title="网格模式">
        <span class="icon icon-btn-switch-grid"></span>
      </a>
    </li>
    <li class="item">
      <a href="#" class="J_Ajax J_SortbarStyle link icon-tag " data-url="default" data-key="style" data-value="list" title="列表模式">
        <span class="icon icon-btn-switch-list"></span>
      </a>
    </li>
  </ul>
</div>

      

      
        <div class="location J_LaterHover" data-hover-cls="location-hover icon-tag" data-leave-timer="504">
  <div class="trigger" tabindex="0" role="group" aria-label="发货地区选择">
    <div class="inner">
      <span class="text" title="">发货地</span>
      <span class="icon icon-btn-arrow-2-h"></span>
    </div>
  </div>
  <div class="sections">
    <div class="section">
      

      <div class="misc g-clearfix">
        
          <div class="guess">同城: <a class="J_Ajax user-loc" href="#" data-url="sortbar" data-key="loc" data-value="上海" trace="seller_location" trace-tracetype="1_上海">上海</a></div>
        

        
      </div>

    </div>

    
      <div class="section">
        
        <ul class="items g-clearfix">
          
            <li class="item">
              <a href="#" class="J_Ajax link align-left" data-url="sortbar" data-key="loc" data-value="%E5%8C%97%E4%BA%AC" trace="seller_location" trace-tracetype="3_北京">北京</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link align-left" data-url="sortbar" data-key="loc" data-value="%E4%B8%8A%E6%B5%B7" trace="seller_location" trace-tracetype="3_上海">上海</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link align-left" data-url="sortbar" data-key="loc" data-value="%E5%B9%BF%E5%B7%9E" trace="seller_location" trace-tracetype="3_广州">广州</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link align-left" data-url="sortbar" data-key="loc" data-value="%E6%B7%B1%E5%9C%B3" trace="seller_location" trace-tracetype="3_深圳">深圳</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link align-left" data-url="sortbar" data-key="loc" data-value="%E6%9D%AD%E5%B7%9E" trace="seller_location" trace-tracetype="3_杭州">杭州</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link align-left" data-url="sortbar" data-key="loc" data-value="%E7%BE%8E%E5%9B%BD%2C%E8%8B%B1%E5%9B%BD%2C%E6%B3%95%E5%9B%BD%2C%E7%91%9E%E5%A3%AB%2C%E6%BE%B3%E5%A4%A7%E5%88%A9%E4%BA%9A%2C%E6%96%B0%E8%A5%BF%E5%85%B0%2C%E5%8A%A0%E6%8B%BF%E5%A4%A7%2C%E5%A5%A5%E5%9C%B0%E5%88%A9%2C%E9%9F%A9%E5%9B%BD%2C%E6%97%A5%E6%9C%AC%2C%E5%BE%B7%E5%9B%BD%2C%E6%84%8F%E5%A4%A7%E5%88%A9%2C%E8%A5%BF%E7%8F%AD%E7%89%99%2C%E4%BF%84%E7%BD%97%E6%96%AF%2C%E6%B3%B0%E5%9B%BD%2C%E5%8D%B0%E5%BA%A6%2C%E8%8D%B7%E5%85%B0%2C%E6%96%B0%E5%8A%A0%E5%9D%A1%2C%E5%85%B6%E5%AE%83%E5%9B%BD%E5%AE%B6" trace="seller_location" trace-tracetype="3_海外">海外</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E6%B1%9F%E8%8B%8F%2C%E6%B5%99%E6%B1%9F%2C%E4%B8%8A%E6%B5%B7" trace="seller_location" trace-tracetype="3_江浙沪">江浙沪</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E5%B9%BF%E5%B7%9E%2C%E6%B7%B1%E5%9C%B3%2C%E4%B8%AD%E5%B1%B1%2C%E7%8F%A0%E6%B5%B7%2C%E4%BD%9B%E5%B1%B1%2C%E4%B8%9C%E8%8E%9E%2C%E6%83%A0%E5%B7%9E" trace="seller_location" trace-tracetype="3_珠三角">珠三角</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E5%8C%97%E4%BA%AC%2C%E5%A4%A9%E6%B4%A5%2C%E6%B2%B3%E5%8C%97" trace="seller_location" trace-tracetype="3_京津冀">京津冀</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E9%BB%91%E9%BE%99%E6%B1%9F%2C%E5%90%89%E6%9E%97%2C%E8%BE%BD%E5%AE%81" trace="seller_location" trace-tracetype="3_东三省">东三省</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E9%A6%99%E6%B8%AF%2C%E6%BE%B3%E9%97%A8%2C%E5%8F%B0%E6%B9%BE" trace="seller_location" trace-tracetype="3_港澳台">港澳台</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E6%B1%9F%E8%8B%8F%2C%E6%B5%99%E6%B1%9F%2C%E4%B8%8A%E6%B5%B7%2C%E5%AE%89%E5%BE%BD" trace="seller_location" trace-tracetype="3_江浙沪皖">江浙沪皖</a>
            </li>
          
        </ul>
      </div>
    
      <div class="section">
        
          <div class="hr-line"></div>
        
        <ul class="items g-clearfix">
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E9%95%BF%E6%B2%99" trace="seller_location" trace-tracetype="3_长沙">长沙</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E9%95%BF%E6%98%A5" trace="seller_location" trace-tracetype="3_长春">长春</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E6%88%90%E9%83%BD" trace="seller_location" trace-tracetype="3_成都">成都</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E9%87%8D%E5%BA%86" trace="seller_location" trace-tracetype="3_重庆">重庆</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E5%A4%A7%E8%BF%9E" trace="seller_location" trace-tracetype="3_大连">大连</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E4%B8%9C%E8%8E%9E" trace="seller_location" trace-tracetype="3_东莞">东莞</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E4%BD%9B%E5%B1%B1" trace="seller_location" trace-tracetype="3_佛山">佛山</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E7%A6%8F%E5%B7%9E" trace="seller_location" trace-tracetype="3_福州">福州</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E8%B4%B5%E9%98%B3" trace="seller_location" trace-tracetype="3_贵阳">贵阳</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E5%90%88%E8%82%A5" trace="seller_location" trace-tracetype="3_合肥">合肥</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E9%87%91%E5%8D%8E" trace="seller_location" trace-tracetype="3_金华">金华</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E6%B5%8E%E5%8D%97" trace="seller_location" trace-tracetype="3_济南">济南</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E5%98%89%E5%85%B4" trace="seller_location" trace-tracetype="3_嘉兴">嘉兴</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E6%98%86%E6%98%8E" trace="seller_location" trace-tracetype="3_昆明">昆明</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E5%AE%81%E6%B3%A2" trace="seller_location" trace-tracetype="3_宁波">宁波</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E5%8D%97%E6%98%8C" trace="seller_location" trace-tracetype="3_南昌">南昌</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E5%8D%97%E4%BA%AC" trace="seller_location" trace-tracetype="3_南京">南京</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E9%9D%92%E5%B2%9B" trace="seller_location" trace-tracetype="3_青岛">青岛</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E6%B3%89%E5%B7%9E" trace="seller_location" trace-tracetype="3_泉州">泉州</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E6%B2%88%E9%98%B3" trace="seller_location" trace-tracetype="3_沈阳">沈阳</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E8%8B%8F%E5%B7%9E" trace="seller_location" trace-tracetype="3_苏州">苏州</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E5%A4%A9%E6%B4%A5" trace="seller_location" trace-tracetype="3_天津">天津</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E6%B8%A9%E5%B7%9E" trace="seller_location" trace-tracetype="3_温州">温州</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E6%97%A0%E9%94%A1" trace="seller_location" trace-tracetype="3_无锡">无锡</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E6%AD%A6%E6%B1%89" trace="seller_location" trace-tracetype="3_武汉">武汉</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E8%A5%BF%E5%AE%89" trace="seller_location" trace-tracetype="3_西安">西安</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E5%8E%A6%E9%97%A8" trace="seller_location" trace-tracetype="3_厦门">厦门</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E9%83%91%E5%B7%9E" trace="seller_location" trace-tracetype="3_郑州">郑州</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E4%B8%AD%E5%B1%B1" trace="seller_location" trace-tracetype="3_中山">中山</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E7%9F%B3%E5%AE%B6%E5%BA%84" trace="seller_location" trace-tracetype="3_石家庄">石家庄</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E5%93%88%E5%B0%94%E6%BB%A8" trace="seller_location" trace-tracetype="3_哈尔滨">哈尔滨</a>
            </li>
          
        </ul>
      </div>
    
      <div class="section">
        
          <div class="hr-line"></div>
        
        <ul class="items g-clearfix">
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E5%AE%89%E5%BE%BD" trace="seller_location" trace-tracetype="3_安徽">安徽</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E7%A6%8F%E5%BB%BA" trace="seller_location" trace-tracetype="3_福建">福建</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E7%94%98%E8%82%83" trace="seller_location" trace-tracetype="3_甘肃">甘肃</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E5%B9%BF%E4%B8%9C" trace="seller_location" trace-tracetype="3_广东">广东</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E5%B9%BF%E8%A5%BF" trace="seller_location" trace-tracetype="3_广西">广西</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E8%B4%B5%E5%B7%9E" trace="seller_location" trace-tracetype="3_贵州">贵州</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E6%B5%B7%E5%8D%97" trace="seller_location" trace-tracetype="3_海南">海南</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E6%B2%B3%E5%8C%97" trace="seller_location" trace-tracetype="3_河北">河北</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E6%B2%B3%E5%8D%97" trace="seller_location" trace-tracetype="3_河南">河南</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E6%B9%96%E5%8C%97" trace="seller_location" trace-tracetype="3_湖北">湖北</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E6%B9%96%E5%8D%97" trace="seller_location" trace-tracetype="3_湖南">湖南</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E6%B1%9F%E8%8B%8F" trace="seller_location" trace-tracetype="3_江苏">江苏</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E6%B1%9F%E8%A5%BF" trace="seller_location" trace-tracetype="3_江西">江西</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E5%90%89%E6%9E%97" trace="seller_location" trace-tracetype="3_吉林">吉林</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E8%BE%BD%E5%AE%81" trace="seller_location" trace-tracetype="3_辽宁">辽宁</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E5%AE%81%E5%A4%8F" trace="seller_location" trace-tracetype="3_宁夏">宁夏</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E9%9D%92%E6%B5%B7" trace="seller_location" trace-tracetype="3_青海">青海</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E5%B1%B1%E4%B8%9C" trace="seller_location" trace-tracetype="3_山东">山东</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E5%B1%B1%E8%A5%BF" trace="seller_location" trace-tracetype="3_山西">山西</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E9%99%95%E8%A5%BF" trace="seller_location" trace-tracetype="3_陕西">陕西</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E4%BA%91%E5%8D%97" trace="seller_location" trace-tracetype="3_云南">云南</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E5%9B%9B%E5%B7%9D" trace="seller_location" trace-tracetype="3_四川">四川</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E8%A5%BF%E8%97%8F" trace="seller_location" trace-tracetype="3_西藏">西藏</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E6%96%B0%E7%96%86" trace="seller_location" trace-tracetype="3_新疆">新疆</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E6%B5%99%E6%B1%9F" trace="seller_location" trace-tracetype="3_浙江">浙江</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E6%BE%B3%E9%97%A8" trace="seller_location" trace-tracetype="3_澳门">澳门</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E9%A6%99%E6%B8%AF" trace="seller_location" trace-tracetype="3_香港">香港</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E5%8F%B0%E6%B9%BE" trace="seller_location" trace-tracetype="3_台湾">台湾</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E5%86%85%E8%92%99%E5%8F%A4" trace="seller_location" trace-tracetype="3_内蒙古">内蒙古</a>
            </li>
          
            <li class="item">
              <a href="#" class="J_Ajax link " data-url="sortbar" data-key="loc" data-value="%E9%BB%91%E9%BE%99%E6%B1%9F" trace="seller_location" trace-tracetype="3_黑龙江">黑龙江</a>
            </li>
          
        </ul>
      </div>
    


    <div class="g-clearfix search">
      <input class="J_SortbarLocationInput input" placeholder="多个地区用逗号分隔" value="">
      <span class="J_SortbarLocationSubmit J_SortbarLocationPopupClose btn" tabindex="0" role="button" aria-label="确定" trace="seller_location" trace-tracetype="4_">确定</span>
    </div>
  </div>
</div>


      
    </div>
  </div>

  <div class="filter-row">
    <div class="filter-box J_LaterHover" data-hover-cls="filter-box-hover" role="group" aria-label="筛选项">
  <div class="filter-inner">
    <div class="filters">
      
        <a class="filter icon-tag J_Ajax " trace="filterbox" trace-filterid="filter_baoyou" href="#" data-url="filter" data-key="baoyou" data-value="1">
          <span class="icon icon-btn-check-big"></span>
          
            <span class="text ">包邮</span>
          
        </a>
      
        <a class="filter icon-tag J_Ajax " trace="filterbox" trace-filterid="filterYunFeiXian" href="#" data-url="filter" data-key="auction_tag[]" data-value="385">
          <span class="icon icon-btn-check-big"></span>
          
            <span class="text ">赠送退货运费险</span>
          
        </a>
      
        <a class="filter icon-tag J_Ajax " trace="filterbox" trace-filterid="filterServiceCOD" href="#" data-url="filter" data-key="support_cod" data-value="1">
          <span class="icon icon-btn-check-big"></span>
          
            <span class="text ">货到付款</span>
          
        </a>
      
        <a class="filter icon-tag J_Ajax " trace="filterbox" trace-filterid="xinpinshangshi" href="#" data-url="filter" data-key="auction_tag[]" data-value="1154">
          <span class="icon icon-btn-check-big"></span>
          
            <span class="text ">新品</span>
          
        </a>
      
        <a class="filter icon-tag J_Ajax " trace="filterbox" trace-filterid="gongyibaobei" href="#" data-url="filter" data-key="gybb" data-value="1">
          <span class="icon icon-btn-check-big"></span>
          
            <span class="text ">公益宝贝</span>
          
        </a>
      
        <a class="filter icon-tag J_Ajax " trace="filterbox" trace-filterid="filter_ershou" href="#" data-url="filter" data-key="filterFineness" data-value="1">
          <span class="icon icon-btn-check-big"></span>
          
            <span class="text ">二手</span>
          
        </a>
      
        <a class="filter icon-tag J_Ajax " trace="filterbox" trace-filterid="filter_tianmao" href="#" data-url="filter" data-key="filter_tianmao" data-value="tmall">
          <span class="icon icon-btn-check-big"></span>
          
            <span class="text ">天猫</span>
          
        </a>
      
        <a class="filter icon-tag J_Ajax " trace="filterbox" trace-filterid="filterProtectionQuality" href="#" data-url="filter" data-key="user_type" data-value="1">
          <span class="icon icon-btn-check-big"></span>
          
            <span class="text ">正品保障</span>
          
        </a>
      
        <a class="filter icon-tag J_Ajax " trace="filterbox" trace-filterid="tuihuochengnuo" href="#" data-url="filter" data-key="auction_tag[]" data-value="4806">
          <span class="icon icon-btn-check-big"></span>
          
            <span class="text ">7+天内退货</span>
          
        </a>
      
        <a class="filter icon-tag J_Ajax " trace="filterbox" trace-filterid="filterServiceOversea" href="#" data-url="filter" data-key="globalbuy" data-value="1">
          <span class="icon icon-btn-check-big"></span>
          
            <span class="text ">海外商品</span>
          
        </a>
      
        <a class="filter icon-tag J_Ajax " trace="filterbox" trace-filterid="filter_commonsort" href="#" data-url="filter" data-key="commonsort" data-value="1">
          <span class="icon icon-btn-check-big"></span>
          
            <span class="text ">通用排序</span>
          
        </a>
      
    </div>
    
      <div class="more">
        <span class="text">更多</span>
        <span class="icon icon-btn-arrow-2-h"></span>
      </div>
    
  </div>
</div>


    <div class="extra">
      
      
    </div>

  </div>

</div>
'''
page = BeautifulSoup(html, 'lxml')
print(page.find('span',class_='current').parent.get_text())