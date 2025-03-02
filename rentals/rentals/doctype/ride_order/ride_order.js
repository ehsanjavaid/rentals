// Copyright (c) 2025, Ahsan and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
  onload(frm) {
    console.log("on running.....!");
  },
  setup(frm) {
    console.log("setup....");
  },

  refresh(frm) {
    console.log("on refresh....");
    {
          if (frm.doc.status === "New") {
              frm.add_custom_button("Accept", () => {
                  //status will be accepted
                  frm.set_value("status", "Accepted");
                  // save form
                  frm.save();
              }, "Actions");
              frm.add_custom_button("Rejected", () => {
                //status will be accepted
                frm.set_value("status", "Rejected");
                // save form
                frm.save();
            }, "Actions");
          }
    }
  },
});
