/* ========================================================

Field Validator
Notes: Field Validator requires the jQuery plugin
Author: David Raffauf
Date: July 1st, 2010

===========================================================*/

function Field(id, type, displayLabel, isRequired) {
	this.id = id;
	this.type = type;
	this.displayLabel = displayLabel;
	this.isRequired = isRequired;
}


function FieldValidator(isSilent, errorClassInput, errorClassLabel, errorClassSelect, errorDisplayClass) {
	// Should we display an alert with all the errors?
	this.isSilent = isSilent;

	// These are the classes with which we are marking errors in the DOM
	this.errorClass = new Array();
	this.errorClass["text"]		= errorClassInput;
	this.errorClass["label"]	= errorClassLabel;
	this.errorClass["select"]	= errorClassSelect;	
	this.errorDisplayClass		= errorDisplayClass;

	// We need a way to store a bunch of fields
	this.formFields = new Array();

	// Create a place to store the errors
	this.errors = "";



	this.add = function(id, type, displayLabel, isRequired) {
		this.formFields[this.formFields.length] = new Field(id, type, displayLabel, isRequired);
	}

	this.print = function() {
		var message = "";

		for(var i in this.formFields) {
			var formField = this.formFields[i];

			message += "id: " + formField.id + ", ";
			message += "type: " + formField.type + ", ";
			message += "guideText: " + formField.displayLabel + ", ";
			message += "isRequired: " + formField.isRequired;

			window.alert(message);
		}				
	}

	this.validate = function() {
		// Reset the error messages
		this.resetErrors();

		// Let's check for valid fields
		for(var i in this.formFields) {			
			var formField = this.formFields[i];
			var element = jQuery("#" + formField.id);
			var value = element.val();

			// Is this field required and if so, does is it set to the guide text?
			if (formField.isRequired && value == "" && formField.type != "checkbox") {
				this.markField(element, this.errorClass["text"]);
				this.markEmptyRequiredField(formField);
			}
			else if (value == formField.displayLabel) {
				this.markField(element, this.errorClass["text"]);
				this.markEmptyRequiredField(formField);
			}
			// It's not required, it doesn't have the default text, and it may be a checkbox
			else {
				this.unMarkField(element, this.errorClass["text"]);
				
				// Check for valid formats
				if (formField.isRequired) {
					switch (formField.type) {
						case "checkbox" :
							this.validateCheckbox(formField);
							break;
						case "select" :
							this.validateSelect(formField);
							break;
						case "zip" :
							this.validateZipCode(formField);
							break;
						case "email" :
							this.validateEmail(formField);
							break;
						case "usPhone" :
							this.validateUSPhone(formField);
							break;
						case "date" :
							this.validateDate(formField);
							break;
						case "radio" :
							this.validateRadio(formField);
							break;
						default:								
					}
				}				
			}
		}

		// Do we have any error messages?
		if (this.hasErrors()) {
			if (!this.isSilent) { this.showErrors(); }
			return false;
		}
		else {
			return true;
		}
	}



	this.markEmptyRequiredField = function(formField) {
		this.addError(formField.displayLabel + " is a required field.");
	}			

	this.validateCheckbox = function(formField) {
		var element = jQuery("#" + formField.id);

		if (element.is(':checked')) {
			this.unMarkField(element.next(), this.errorClass["label"]);
		}
		else if(element.not(':checked')) {
			this.markField(element.next(), this.errorClass["label"]);
			this.addError(formField.displayLabel + ": checkbox must be checked.");
		}
	}


	this.validateSelect = function(formField) {
		var element = jQuery("#" + formField.id);

		if (element.attr("selectedIndex") == 0)  {
			this.markField(element, this.errorClass["select"]);
			this.addError(formField.displayLabel + ": Please choose a selection.");
		}
		else {
			this.unMarkField(element, this.errorClass["select"]);
		}
	}


	this.validateZipCode = function(formField) {
		var format=/^\d{5}$/;
		var element = jQuery("#" + formField.id);

		if (!format.test(element.val())) {
			// This doesn't have five characters
			element.val(formField.displayLabel);
			this.markField(element, this.errorClass["text"]);
			this.addError(formField.displayLabel + ": must contain 5 digits only.");
		}
		else {
			this.unMarkField(element, this.errorClass["text"]);
			element.removeClass(this.errorClass["text"]);
		}
	}


	this.validateRadio = function(formField) {
		var element = $('input:radio[name=' + formField.id + ']:checked');
		var value = element.val();

		if(!value) {
			element = $('input:radio[name=' + formField.id + ']'); 			
			this.markField($('label[for=' + formField.id + ']'), this.errorClass["label"]);
			this.addError(formField.displayLabel + ": an option must be selected.");
		}
		else {
			var displayLabel = $('label[for=' + formField.id + ']');
			this.unMarkField(displayLabel, this.errorClass["label"]);
		}		
	}


	this.validateEmail = function(formField) {
		var format=/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
		var element = jQuery("#" + formField.id);

		if (!format.test(element.val())) {
			element.val(formField.displayLabel)
			this.markField(element, this.errorClass["text"]);
			this.addError("Please enter a valid email address.");
		}
		else {
			this.unMarkField(element, this.errorClass["text"]);				}
	}


	this.validateUSPhone = function(formField) {
		var element = jQuery("#" + formField.id);

		var format1=/^\d{10}$/;
		var format2=/^\d{3}\s\d{3}\s\d{4}$/;
		var format3=/^\(\d{3}\)\s*\d{3}-\d{4}$/;
		var format4=/^\d{3}\.\d{3}\.\d{4}$/;

		if (!format1.test(element.val()) &&
			!format2.test(element.val()) &&
			!format3.test(element.val()) &&
			!format4.test(element.val())) {
			element.val(formField.displayLabel)
			this.markField(element, this.errorClass["text"]);
			this.addError("Please enter a valid phone number.");
		}
		else {
			this.unMarkField(element, this.errorClass["text"]);					
		}
	}


	this.validateDate = function(formField) {
		var format=/^\d{2}\/\d{2}\/\d{4}$/;
		var element = jQuery("#" + formField.id);
		var value = element.val();

		if (!format.test(element.val())) {
			element.val("MM/DD/YYYY");
			this.markField(element, this.errorClass["text"]);
			this.addError("Dates must match this format: MM/DD/YYYY.");
		}
		else {
			// Type specific fields
			var monthfield	= value.split("/")[0]
			var dayfield	= value.split("/")[1]
			var yearfield	= value.split("/")[2]
			var dayobj 		= new Date(yearfield, monthfield-1, dayfield)

			// Check the month, day and year
			if ((dayobj.getMonth()+1!=monthfield) || 		
				(dayobj.getDate()!=dayfield) ||
				(dayobj.getFullYear()!=yearfield)) {
				this.markField(element, this.errorClass["text"]);
				element.val("MM/DD/YYYY");
				this.addError("The day, month or year provided is invalid.");
			}
		}
	}



	this.getElementById = function(id) {
		return jQuery("#" + id);
	}

	this.unMarkField = function(element, myClass) {
		element.removeClass(myClass);
	}

	this.markField = function(element, myClass) {
		element.addClass(myClass);				
	}



	this.addError = function(message) {			
		this.errors += message + "<br />";
	}

	this.hasErrors = function() {
		if (this.errors == "")
			return false;
		else
			return true;
	}

	this.showErrors = function() {
		if (this.hasErrors()) {
			element = jQuery("." + this.errorDisplayClass);
			element.html(this.errors);
			element.show();
		}
	}

	this.resetErrors = function() {
		element = jQuery("." + this.errorDisplayClass);
		element.html("");
		element.hide();
		this.errors = "";
	}
}