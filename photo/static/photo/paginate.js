//Reference Code: https://github.com/LaminSanneh/Jquery-Pagination-Plugin/archive/master.zip
//Javascript to handle Pagination Control

(function($){

    $(document).ready(function(){
            //Pagination Container Details added
           var paginationContainer = $(".pagination");
           // Item to be paginated
           var itemsToPaginate=$(".thumbnailrows");
           //Number of Items per page
           var itemsPerPage = 10;
           //Class definition for the li which needs to be made active
           var activeClass="active-class";

            // Number of Page Links to be generated
           var numberOfPaginationLinks = Math.ceil((itemsToPaginate.length / itemsPerPage));

            //Add <ul> to the pagination div to house the li for the navigation
           $("<ul class=\"pagination-sm\"></ul>").prependTo(paginationContainer);

            //Add as many li as required
           for(var index = 0; index < numberOfPaginationLinks; index++)
           {
                paginationContainer.find("ul").append("<li><a href=\"#\">"+ (index+1) + "</a></li>");
           }

            //Hide any items greater than items per page
           itemsToPaginate.filter(":gt(" + (itemsPerPage - 1)  + ")").hide();

            //Navigation
           paginationContainer.find("ul li").first().addClass(activeClass).end().on('click', function(){
                //Change the "active-class" for the li
			   var $this = $(this);

			   $this.addClass(activeClass);

			   $this.siblings().removeClass(activeClass);

               var linkNumber = $this.text();

                //Hide any item which does not belong to the link li which is being clicked
                var itemsToHide = itemsToPaginate.filter(":lt(" + ((linkNumber-1) * itemsPerPage)  + ")");
                $.merge(itemsToHide, itemsToPaginate.filter(":gt(" + ((linkNumber * itemsPerPage) - 1)  + ")"));
                //Show the items which are not to be hidden
                var itemsToShow = itemsToPaginate.not(itemsToHide);

                //Adjust the html and body to show the items to be shown and hide items to be hidden
                $("html,body").animate({scrollTop:"0px"}, function(){
                  itemsToHide.hide();
                  itemsToShow.show();
                });
           });

       });

})(jQuery)