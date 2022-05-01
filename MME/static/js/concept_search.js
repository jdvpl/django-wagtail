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

  template = `
      <tbody>

            <tr>
              <td>${ item.sectors_list }</td>
              <td>${ item.year_list }</td>
              <td>${ item.settled_number }</td>
              <td>${ item.settled_date }</td>
              <td>${ item.norm }</td>
              <td>${ item.petitioner }</td>
              <td>${ item.subject }</td>
              <td>
                  <a class="btn btn btn-success" href="${ item.url }">Ver más</a>
              </td>
          </tr>
      </tbody>

  </table>`;

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
  let anioSelect = document.getElementById("anio");
  let anio = anioSelect.options[anioSelect.selectedIndex].text;
  let radicado = document.getElementById("radicado").value;
  let norma = document.getElementById("norma").value;
  let petici = document.getElementById("peticionario").value;


  if (
    dateRange.length > 0 ||
    yearMonth.length > 0 ||
    keywords.length > 0 ||
    sector != "Seleccione un sector" ||
    anio != "Seleccione un año" ||
    radicado != "" ||
    norma    != "" ||
    petici   != ""

  ) {
    searchData(dateRange, yearMonth, keywords, sector, anio, radicado, norma, petici);
  }
});
//limpia el formulario
document.getElementById("clearForm").addEventListener("click", function () {
  document.getElementById("keywords").value = "";
  let sectorSelect = document.getElementById("sector");
  sectorSelect.options[0].selected = true;
  let anioSelect = document.getElementById("anio");
  anioSelect.options[0].selected = true;
  document.getElementById("radicado").value = "";
  document.getElementById("norma").value = "";
  document.getElementById("peticionario").value = "";
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
    let itemDate = new Date(dataset.items[i].settled_date + " 00:00:00");
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
    let itemDate = new Date(dataset.items[i].settled_date);
    let itemyear = itemDate.getYear();
    if (itemyear === year) {
      auxfilter.push(dataset.items[i]);
    }
  }
  for (var i = 0; i < auxfilter.length; i++) {
    let itemDate = new Date(auxfilter[i].settled_date);
    let itemmonth = itemDate.getMonth();
    if (itemmonth === month) {
      filterDataSet.push(dataset.items[i]);
    }
  }
};
//filtro por palabbras claves en asunto
filterbykeywords = (keywords, data) => {
  let aux = keywords.toLowerCase().replace(" ", "");
  aux = aux.split(",");
  let auxfilter = [];
  let controli = [];
  for (var i = 0; i < data.length; i++) {
    let tags = data[i].subject;
//crea un array por espacios
    let asun = tags.split(" ");
    for (var j = 0; j < aux.length; j++) {
      for (var z = 0; z < asun.length; z++) {
        if (asun[z].toLowerCase() === aux[j] && controli.includes(i) == false) {
          controli.push(i);
            auxfilter.push(data[i]);
        }
      }
    }
  }
  filterDataSet = auxfilter;
};
//filtro por sectores
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

//filtro por año
filterbyanios = (anio, data) => {

  let aux_a = anio.toLowerCase();

  let auxfilter = [];
  for (var i = 0; i < data.length; i++) {
    let year_list = data[i].year_list;
    for (var z = 0; z < year_list.length; z++) {
     if (year_list[z].toLowerCase() === aux_a) {
        auxfilter.push(data[i]);
      }
    }
  }
  filterDataSet = auxfilter;
};
//filtro por radicado
filterbyradicados = (radicado, data) => {

  let aux = radicado;

  let auxfilter = [];
  for (var i = 0; i < data.length; i++) {
    let settled_number = data[i].settled_number;
      if (settled_number === aux) {

        auxfilter.push(data[i]);
      }

  }
  filterDataSet = auxfilter;
};

// filtro para norma

filterbynorma = (norma, data) => {
  let aux = norma.toLowerCase();
  aux = aux.split(" ");
  let auxfilter = [];
  let controli = [];
  for (var i = 0; i < data.length; i++) {
    let tags = data[i].norm.replace(",", "");
//crea un array por espacios
    let asun = tags.split(" ");
    for (var j = 0; j < aux.length; j++) {
      for (var z = 0; z < asun.length; z++) {
        if (asun[z].toLowerCase() === aux[j] && controli.includes(i) == false) {
          controli.push(i);
            auxfilter.push(data[i]);
        }
      }
    }
  }
  filterDataSet = auxfilter;
};

// filtro para peticionario
filterbypetici = (petici, data) => {
  let aux = petici.toLowerCase();
  aux = aux.split(" ");
  let auxfilter = [];
let controli = [];
  for (var i = 0; i < data.length; i++) {
    let tags = data[i].petitioner;
    for (var j = 0; j < aux.length; j++) {
      let index = tags.toLowerCase().includes(aux[j]);
//si lo encuentra, verifica que no repita registro con controli
          if (index > 0 && controli.includes(i) == false) {
          controli.push(i);
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

searchData = (dateRange, yearMonth, keywords, sectors, anio, radicado, norma, petici) => {
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

  if (anio != "Seleccione un año") {
    filterbyanios(anio, filterDataSet);
  }

  if (radicado != "") {
    filterbyradicados(radicado, filterDataSet);
  }

  if (norma != "") {
    filterbynorma(norma, filterDataSet);
  }

  if (petici != "") {
    filterbypetici(petici, filterDataSet);
  }


  buildnewtable(filterDataSet);
};

/* Advanced-Search */

/* get dataset */
getDataSet = () => {
  fetch(`/api/v2/pages/?type=${page}&fields=*`)
    .then((res) => res.json())
    .then(function (data) {
      dataset = data;
      console.log(data);
    })
    .catch((err) => console.error(err));
};
/* get dataset */

document.addEventListener("DOMContentLoaded", function () {
  buildTable();
  getDataSet();
});
