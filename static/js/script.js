
//generate a random price
function randomPrice() {
  const prices = [49, 29, 30, 20, 19, 45, 10, 9, 15, 5];
  let index = Math.floor(Math.random() * prices.length);
   return prices[index];
}

//truncate string at a specified length, then add ...
function truncateString(str) {
  //splice string from 0 to len, exclude char at len
  return (str.length > 20) ? str.slice(0, 20).concat('...') : str;
}


$(document).ready(() => {
  
  $.ajax({
    url: 'https://api.punkapi.com/v2/beers',
    type: 'GET',
    dataType: 'json'
    
  }).done((beers) => {
    console.log(beers);
    let $row = $('.row');
    beers.forEach((beer) => {
      
      let price = randomPrice();
      
    $row.append(`<div class="col-sm-12 col-md-6 col-lg-4">
           <article class="card my-3 shadow-sm" data-id="${beer.id}">
             <img class="card-img-top" src="${beer.image_url}" alt="${beer.name}">
            <div class="card-body">
              <div class="d-flex justify-content-between">
               <h5 class="card-title">${truncateString(beer.name)}</h5>
               <h5 class="card-text">$${price}.00</h5>
             </div>
             <button type="button" class="btn btn-block btn-outline-teal mt-1" tabindex="-1" data-toggle="modal" data-target="#modal-${beer.id}">
             <i class="far fa-eye"></i> Quick View</button>
            </div>
          </article>
             <div class="modal fade" id="modal-${beer.id}">
              <div class="modal-lg modal-dialog modal-dialog-centered modal-dialog-scrollable" role="document">
                <div class="modal-content">
                  <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-label="close">
                                                <span aria-hidden="true">&times;</span>
                                            </button>
                  </div>
                  <div class="modal-body">
                    <div class="row">
                      <div class="col-12 col-lg-5">
                        <img src="${beer.image_url}" alt="${beer.name}">
                      </div>
                      <div class="col-12 col-lg-7">
                        <article class="px-2">
                          <h2 class="mt-2">${beer.name}</h2>
                          <span class="text-muted">${beer.tagline}</span>
                          <h3 class="mt-2">$${price}.00</h3>
                          <p><span class="text-muted">Volume:</span>
                          <strong>${beer.volume.value} ${beer.volume.unit}</strong></p>
                          <p>${beer.description}</p>
                          <form class="mt-2 d-flex align-content-center">
                            <input type="number" name="quantity" class="w-25 form-control" min="1">
                            <button class="ml-2 btn btn-outline-teal">
                            <i class="fas fa-shopping-bag"></i>
                             Add to Cart</button>
                          </form>
                        </article>
                      </div>
                    </div>
                  </div>
                  <div class="modal-footer">
                  </div>
                </div>
              </div>
              </div>
        </div>`);
     });
  }).fail(() => {
    console.log('someting went wrong!');
  });

}); 
