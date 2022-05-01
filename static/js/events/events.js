let events_count = 0;
let dataset = {};

/* format date for modal event title */
getEventDateFormat = (date) => {
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
/* format date for modal event title */

/* builder the modal for events list */
buildModalTemplate = (date) => {
  let modalTitle = "";
  let modalEventsList = "";
  let modalContent = "";

  modalTitle = `<h5 class="modal-title text-center" id="eventModalLabel"> Eventos programados para ${getEventDateFormat(
    date
  )} </h5>`;

  for (let index = 0; index < events_count; index++) {
    if (dataset.items[index].date_published === date) {
      modalEventsList += `<a href="${dataset.items[index].meta.html_url}" class="list-group-item list-group-item-action">${dataset.items[index].title}</a>`;
    }
  }

  modalContent = `<div class="modal-header">
                        <h5 class="modal-title text-center" id="eventModalLabel">${modalTitle}</h5>
                        <button type="button" class="btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body" style="background-color: white;color:black">
                            <div class="list-group">
                                ${modalEventsList}
                            </div>
                        </div>`;

  return modalContent;
};
/* builder the modal for events list */

/* check if day has events and start the modal */
checkEventinItems = (date) => {
  for (let index = 0; index < events_count; index++) {
    if (dataset.items[index].date_published === date) {
      var eventModal = new bootstrap.Modal(
        document.getElementById("eventModal"),
        {
          keyboard: false,
        }
      );
      document.getElementById("modalContent").innerHTML =
        buildModalTemplate(date);
      eventModal.show();
      return;
    }
  }
  return;
};
/* check if day has events and start the modal */

/* check if day has events */
checkEventinCalendar = (dayElem) => {
  for (let index = 0; index < events_count; index++) {
    let event_date = new Date(
      dataset.items[index].date_published + " 00:00:00"
    );
    if (
      dayElem.dateObj.getMonth() === event_date.getMonth() &&
      dayElem.dateObj.getDate() === event_date.getDate()
    ) {
      return true;
    }
  }
  return false;
};
/* check if day has events */

buildEventsCalendar = () => {
  /* sort items ascending */
  dataset.items.sort((a, b) => {
    return new Date(b.date_published) - new Date(a.date_published);
  });
  /* sort items ascending */

  /* set event list limit */
  if (dataset.meta.total_count >= 10) {
    events_count = 10;
  } else {
    events_count = dataset.meta.total_count;
  }
  /* set event list limit */

  flatpickr("#eventsDate", {
    locale: "es",
    altInput: true,
    altFormat: "F j, Y",
    dateFormat: "Y-m-d",
    minDate: dataset.items[events_count - 1].date_published,
    maxDate: dataset.items[0].date_published,
    inline: true,
    onDayCreate: function (dObj, dStr, fp, dayElem) {
      /* add mark if day has events */
      if (checkEventinCalendar(dayElem)) {
        dayElem.innerHTML += "<span class='event'></span>";
      }
      /* add mark if day has events */
    },
    onChange: function (dateObj, dateStr) {
      /* check if day has events and start the modal */
      checkEventinItems(dateStr);
      /* check if day has events and start the modal */
    },
  });
};

document.addEventListener("DOMContentLoaded", function () {
  fetch(`/api/v2/pages/?type=sala_prensa.EventoPage&fields=*`)
    .then((res) => res.json())
    .then(function (data) {
      dataset = data;
      buildEventsCalendar();
    })
    .catch((err) => console.error(err));
});
