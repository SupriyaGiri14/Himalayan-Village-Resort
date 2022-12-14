
var ref_no = ''
$( ".datepicker" ).datepicker({ maxDate: '0' });


function GetDays(){
    var dropdt = new Date(document.getElementById("checkout_date").value);
    var pickdt = new Date(document.getElementById("checkin_date").value);
    return parseInt((dropdt - pickdt) / (24 * 3600 * 1000));
}

function cal_extra_room_rate(){
    alert("inside")
    var total_amount = document.getElementById('total_price').value;
    var no_of_rooms = document.getElementById('no_of_rooms').value;
    no_of_days = GetDays();
    document.getElementById('total_price').value = 3500 * no_of_rooms * no_of_days
}

function cal(){
    
    let no_of_days;
    var check_in_date = new Date(document.getElementById('checkin_date').value);
    var check_out_date = new Date(document.getElementById('checkout_date').value);
    var no_of_rooms = document.getElementById('no_of_rooms').value;
   
    if (check_in_date.getTime() == check_out_date.getTime()) {
    }
    if (check_in_date.getTime() > check_out_date.getTime()) {
    
        alert("The Check Out Date Should be Greater than Check In Date!!");
        document.getElementById('checkout_date').value = ''
    }else{
        if(document.getElementById("checkout_date")){
            no_of_days = GetDays();
            if (no_of_days == 0){
                document.getElementById("no_of_days").value=no_of_days  
                alert('Number of Days can not be Zero!!')
                document.getElementById("total_price").value=0;
            }else{
                document.getElementById("no_of_days").value=no_of_days
                document.getElementById("total_price").value=no_of_days * 3500 * no_of_rooms;
            }
        }
    }  
    if (no_of_days == 0){
        document.getElementById("amount_due").value = 0
        document.getElementById('amount_paid').value = 0
    }else{
    var amount_paid = document.getElementById('amount_paid').value;
    var total_amount = document.getElementById('total_price').value;
    document.getElementById("amount_due").value= total_amount - amount_paid
    if (total_amount != ''){
        if (amount_paid < total_amount){
            alert('a')
            if (amount_paid == 0){
                alert('b')
                document.getElementById("payment_status").selectedIndex = "3";
            }else{
                alert("c")
                document.getElementById("payment_status").selectedIndex = "2";
            }
        }
        else
        {
            if(amount_paid == total_amount){
                document.getElementById("payment_status").selectedIndex = "1";
            }else{
        
                alert("Please check the Amount paid field.It's greater than Total Amount..Correct it if required!!")
            }
        }
    }
    }
}
    

function cal_amount_due(){
    amount_paid = document.getElementById('amount_paid').value;
    total_amount = document.getElementById('total_price').value;
    document.getElementById('amount_due').value = total_amount - amount_paid
}

function search_clicked() {
    ref_no = document.getElementById("search_booking_id").value
    if (ref_no == ''){
        alert('Please select the Bookig-id to Seach!!')
    }
}

function searchbooking_clicked(){
    ref_no = document.getElementById("input_booking_id").value
    if (ref_no == ''){
        alert('Please select the Bookig-id to Seach!!')
    }
}

function delete_clicked() {
    ref_no = ref_no
    if (ref_no != ''){
        let isExecuted = confirm("Are you sure you want to Delete the Booking with Booking id " + ref_no +" ?");
        if (isExecuted){
            console.log(isExecuted); // OK = true, Cancel = false
            $.ajax({
                url: 'admin_manage_booking',
                type:'get',
                data: {
                    ref_no_booking: ref_no,
                    operation:'delete'
                },
                error: function (response) {
                    // alert the error if any error occured
                    alert(response["responseJSON"]["error"]);
                }
            });
        }else{
            ref_no =''
        }
    }
    else{
        alert('Please select the Record to Delete!!')
    }
}


function update_clicked() {
    if (ref_no != ''){
        let isExecuted = confirm("Are you sure you want to Update the Booking with Booking id " + ref_no +" ?");
        if (isExecuted){
            console.log(isExecuted); // OK = true, Cancel = false
            /*$.ajax({
                url: 'admin_manage_booking',
                type:'get',
                data: {
                    ref_no_booking: ref_no,
                    operation:'update'
                },
                success: function (response){ 
                    alert('HH');
                },
                error: function (response) {
                    // alert the error if any error occured
                    alert(response["responseJSON"]["error"]);
                }
            }).done(function (response) {
                window.location.href = 'update_booking' + ref_no
            });*/
        }
        else{
            alert('No')
        }
    }
    else{
        alert('Please select the Record to Update!!')
    }
}


function select_booking(ref_no1){
    ref_no = ref_no1;
}

$(document).ready(function(){  

    $(".datepicker").datepicker({
        minDate: 0,
        maxDate: 2
    });

    var today = new Date().toISOString().split('T')[0];
    $("#checkin_date").attr('min', today);
    $("#checkout_date").attr('min', today);

    $(".carousel").animate({
        width: "100%",
        height: "500px",
        borderWidth: "2px",
        marginLeft: "0px",
    });
    $('#banner-container').hide().delay(400).fadeIn('3000');
    $('#banner-container1').hide().delay(400).fadeIn('3000');


    $(".booking_table").animate({
        width: "400px",
        height: "500px",
        marginLeft: "0px",
        borderWidth: "10px",
        opacity: 0.5
    });
});