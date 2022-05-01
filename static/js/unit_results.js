let datatable;
let dataset = {};

stringnames = (names) => {
  let data = "";
  for (var i = 0; i < names.length - 1; i++) {
    data += names[i] + ", ";
  }
  data += names[names.length - 1];
  return data;
};

getdateformat = (date) => {
  const months = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
  ];
  let newdate = new Date(date + " 00:00:00");
  return `${newdate.getDate()} de ${
    months[newdate.getMonth()]
  } de ${newdate.getFullYear()}`;
};

itemTemplate = (item) => {
  let template = "";
  
    template = `<tr>
      <td>
          <a href="${item.meta.html_url}">
              <div class="container mt-4">
                  <div class="row">
                      <div class="col-xxl-4 col-xl-4 col-lg-12  col-md-12 col-sm-12">
                          <img src="${
                            item.image_data.url
                          }" class="img-fluid" alt="${item.image_data.alt}">
                      </div>
                      <div class="col-xxl-8 col-xl-8 col-lg-12  col-md-12 col-sm-12">
                          <h4 class="news-subtitle news-list-item-title">${
                            item.title
                          } </h4>
                          <p class="fs-5 lh-sm news-list-item-text">
                              ${item.introduction}
                          </p>
                          <p class="fs-6 mt-3">
                              ${getdateformat(
                                item.date_published
                              )}. ${stringnames(item.author_list)}, ${
      item.city
    }.
                          </p>
                          <p class="fs-6">
                              Sector: ${stringnames(item.sectors_list)}
                          </p>
                      </div>

                  </div>
              </div>
          </a>
      </td>
  </tr>`;
  

  return template;
};

/* Table Builder */

buildTable = () => {
  datatable = $("#dataset").DataTable({
    pageLength: pageitems,
    pagingType: "full_numbers",
    searching: false,
    ordering: false,
    lengthChange: false,
    //dom: "itrip",
    dom: '<"top"i>rt<"d-flex justify-content-start" i><"d-flex justify-content-center" p>',
    language: {
      decimal: "",
      emptyTable:
        "<h3>Lo sentimos, no hemos encontrado datos que correspondan con su búsqueda.</h3>",
      info: "Mostrando _START_ a _END_ de _TOTAL_ registros",
      infoEmpty: "Mostrando 0 a 0 de 0 registros",
      infoFiltered: "(filtered from _MAX_ total entries)",
      infoPostFix: "",
      thousands: ",",
      lengthMenu: "Show _MENU_ entries",
      loadingRecords: "Cargando...",
      processing: "Procesando...",
      search: "Search:",
      zeroRecords:
        "No hemos encontrado registros que coincidan con su búsqueda",
      paginate: {
        first:
          '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-chevron-bar-left" viewBox="0 0 16 16">  <path fill-rule="evenodd" d="M11.854 3.646a.5.5 0 0 1 0 .708L8.207 8l3.647 3.646a.5.5 0 0 1-.708.708l-4-4a.5.5 0 0 1 0-.708l4-4a.5.5 0 0 1 .708 0zM4.5 1a.5.5 0 0 0-.5.5v13a.5.5 0 0 0 1 0v-13a.5.5 0 0 0-.5-.5z"/></svg>',
        previous:
          '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-chevron-double-left" viewBox="0 0 16 16">  <path fill-rule="evenodd" d="M8.354 1.646a.5.5 0 0 1 0 .708L2.707 8l5.647 5.646a.5.5 0 0 1-.708.708l-6-6a.5.5 0 0 1 0-.708l6-6a.5.5 0 0 1 .708 0z"/>  <path fill-rule="evenodd" d="M12.354 1.646a.5.5 0 0 1 0 .708L6.707 8l5.647 5.646a.5.5 0 0 1-.708.708l-6-6a.5.5 0 0 1 0-.708l6-6a.5.5 0 0 1 .708 0z"/></svg>',
        next: '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-chevron-double-right" viewBox="0 0 16 16"> <path fill-rule="evenodd" d="M3.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L9.293 8 3.646 2.354a.5.5 0 0 1 0-.708z"/>  <path fill-rule="evenodd" d="M7.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L13.293 8 7.646 2.354a.5.5 0 0 1 0-.708z"/></svg>',
        last: '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-chevron-bar-right" viewBox="0 0 16 16"> <path fill-rule="evenodd" d="M4.146 3.646a.5.5 0 0 0 0 .708L7.793 8l-3.647 3.646a.5.5 0 0 0 .708.708l4-4a.5.5 0 0 0 0-.708l-4-4a.5.5 0 0 0-.708 0zM11.5 1a.5.5 0 0 1 .5.5v13a.5.5 0 0 1-1 0v-13a.5.5 0 0 1 .5-.5z"/> </svg>',
      },
      aria: {
        paginate: {
          first: "First",
          previous: "Previous",
          next: "Next",
          last: "Last",
        },
      },
      aria: {
        sortAscending: ": activate to sort column ascending",
        sortDescending: ": activate to sort column descending",
      },
    },
  });
};
/* Table Builder */

/* Advanced-Search */

/* Datapicker config */
let dateRange = [];
let yearMonth = [];
let filterDataSet = [];

const startTimePicker = flatpickr("#startTime", {
  locale: "es",
  altInput: true,
  altFormat: "F j, Y",
  dateFormat: "Y-m-d",
  minDate: "2020-01",
  maxDate: Date.now(),
  disableMobile: "true",
  plugins: [new rangePlugin({ input: "#endTime" })],

  onChange: function (selectedDates, dateStr) {
    dateRange = selectedDates;
  },
  onOpen: [
    function (selectedDates, dateStr) {
      dateRange = selectedDates;
    },
  ],
  onClose: function (selectedDates, dateStr) {
    yearMonth = [];
    MonthPicker.clear();
  },
});

flatpickr("#endTime", {
  locale: "es",
  altInput: true,
  altFormat: "F j, Y",
  dateFormat: "Y-m-d",
  minDate: "2020-01",
  maxDate: Date.now(),
  disableMobile: "true",
});

const MonthPicker = flatpickr("#month", {
  locale: "es",
  minDate: "2020-01",
  maxDate: Date.now(),
  disableMobile: "true",
  plugins: [
    new monthSelectPlugin({
      shorthand: true,
      dateFormat: "F - Y",
      altFormat: "F - Y",
      theme: "material_blue",
    }),
  ],

  onChange: function (selectedDates, dateStr) {
    yearMonth = selectedDates;
  },
  onOpen: [
    function (selectedDates, dateStr) {
      yearMonth = selectedDates;
    },
  ],
  onClose: function (selectedDates, dateStr) {
    dateRange = [];
    startTimePicker.clear();
  },
});

/* End Datapicker config */

document.getElementById("filterData").addEventListener("click", function () {
  let keywords = document.getElementById("keywords").value;
  let sectorSelect = document.getElementById("sector");
  let sector = sectorSelect.options[sectorSelect.selectedIndex].text;

  if (
    dateRange.length > 0 ||
    yearMonth.length > 0 ||
    keywords.length > 0 ||
    sector != "Seleccione un sector"
  ) {
    searchData(dateRange, yearMonth, keywords, sector);
  }
});

document.getElementById("clearForm").addEventListener("click", function () {
  document.getElementById("keywords").value = "";
  let sectorSelect = document.getElementById("sector");
  sectorSelect.options[0].selected = true;
  startTimePicker.clear();
  MonthPicker.clear();

  buildnewtable(dataset.items);
});

filterbydaterange = (dateRange) => {
  let start = null;
  let end = null;

  if (dateRange.length === 1) {
    start = dateRange[0];
    end = dateRange[0];
  }
  if (dateRange.length === 2) {
    start = dateRange[0];
    end = dateRange[1];
  }

  for (var i = 0; i < dataset.meta.total_count; i++) {
    let itemDate = new Date(dataset.items[i].date_published + " 00:00:00");
    if (itemDate >= start && itemDate <= end) {
      filterDataSet.push(dataset.items[i]);
    }
  }
};

filterbyyearmonth = (yearmonth) => {
  let year = yearmonth[0].getYear();
  let month = yearmonth[0].getMonth();
  let auxfilter = [];

  for (var i = 0; i < dataset.meta.total_count; i++) {
    let itemDate = new Date(dataset.items[i].date_published);
    let itemyear = itemDate.getYear();
    if (itemyear === year) {
      auxfilter.push(dataset.items[i]);
    }
  }
  for (var i = 0; i < auxfilter.length; i++) {
    let itemDate = new Date(auxfilter[i].date_published);
    let itemmonth = itemDate.getMonth();
    if (itemmonth === month) {
      filterDataSet.push(dataset.items[i]);
    }
  }
};

filterbykeywords = (keywords, data) => {
  let aux = keywords.toLowerCase().replace(" ", "");
  aux = aux.split(",");
  let auxfilter = [];

  for (var i = 0; i < data.length; i++) {
    let tags = data[i].tags;
    for (var j = 0; j < aux.length; j++) {
      for (var z = 0; z < tags.length; z++) {
        if (tags[z].toLowerCase() === aux[j]) {
          auxfilter.push(data[i]);
        }
      }
    }
  }
  filterDataSet = auxfilter;
};

filterbysectors = (sectors, data) => {
  let aux = sectors.toLowerCase();

  let auxfilter = [];
  for (var i = 0; i < data.length; i++) {
    let sectors_list = data[i].sectors_list;
    for (var z = 0; z < sectors_list.length; z++) {
      if (sectors_list[z].toLowerCase() === aux) {
        auxfilter.push(data[i]);
      }
    }
  }
  filterDataSet = auxfilter;
};

buildnewtable = (filterDataSet) => {
  newdataset = "";
  datatable.destroy();

  for (var i = 0; i < filterDataSet.length; i++) {
    newdataset += itemTemplate(filterDataSet[i]);
  }
  var tabledataset = document.getElementById("tabledataset");
  tabledataset.innerHTML = "";

  tabledataset.innerHTML = newdataset;

  buildTable();
};

searchData = (dateRange, yearMonth, keywords, sectors) => {
  filterDataSet = [];
  let filter_flag = true;
  if (dateRange.length > 0) {
    filterbydaterange(dateRange);
    filter_flag = false;
  }

  if (yearMonth.length > 0) {
    filterbyyearmonth(yearMonth);
    filter_flag = false;
  }

  if (filterDataSet.length === 0 && filter_flag) {
    filterDataSet = dataset.items;
  }

  if (keywords.length > 0) {
    filterbykeywords(keywords, filterDataSet);
  }

  if (sectors != "Seleccione un sector") {
    filterbysectors(sectors, filterDataSet);
  }

  buildnewtable(filterDataSet);
};

/* Advanced-Search */

/* get dataset */
getDataSet = () => {
  var total_count = 0;
  fetch(`/api/v2/pages/?type=${page}&fields=*`)
    .then((res) => res.json())
    .then(function (data) {
      total_count = data.meta.total_count;
      fetch(`/api/v2/pages/?type=${page}&fields=*&limit=${total_count}`)
        .then((res) => res.json())
        .then(function (data) {
          dataset = data;
        })
        .catch((err) => console.error(err));
    })
    .catch((err) => console.error(err));
};
/* get dataset */

document.addEventListener("DOMContentLoaded", function () {
  buildTable();
  getDataSet();
});
