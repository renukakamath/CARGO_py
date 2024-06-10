package com.example.c_bin;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.Uri;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class Userviewbookedcargo extends AppCompatActivity implements JsonResponse, AdapterView.OnItemClickListener {
    ListView l1;
    String[] oid,bookingdate,weight,length,width,fromlocation,tolocation,amount,bookingstatus,did,value;
    SharedPreferences sh;
    public static String oids,dids,amounts,stat;

    

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_userviewbookedcargo);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        l1=(ListView)findViewById(R.id.lvview);
        l1.setOnItemClickListener(this);

        JsonReq JR=new JsonReq();
        JR.json_response=(JsonResponse)Userviewbookedcargo.this;
        String q="/userviewbookedcargo?lid="+sh.getString("log_id","")+"&bid="+sh.getString("bid","");
        q=q.replace(" ","%20");
        JR.execute(q);
    }

    @Override
    public void response(JSONObject jo) {
        try {


            String status=jo.getString("status");
            Log.d("pearl",status);


            if(status.equalsIgnoreCase("success")){
                JSONArray ja1=(JSONArray)jo.getJSONArray("data");
                oid=new String[ja1.length()];
                bookingdate=new String[ja1.length()];
                bookingstatus=new String[ja1.length()];
                amount=new String[ja1.length()];
                weight=new String[ja1.length()];
                fromlocation=new String[ja1.length()];
                tolocation=new String[ja1.length()];
                length=new String[ja1.length()];
                width=new String[ja1.length()];
                did=new String[ja1.length()];

                value=new String[ja1.length()];

                for(int i = 0;i<ja1.length();i++)
                {
                    did[i]=ja1.getJSONObject(i).getString("boy_id");
                    oid[i]=ja1.getJSONObject(i).getString("booking_id");
                    fromlocation[i]=ja1.getJSONObject(i).getString("from_location");
                    tolocation[i]=ja1.getJSONObject(i).getString("to_location");
                    bookingstatus[i]=ja1.getJSONObject(i).getString("booking_status");
                    bookingdate[i]=ja1.getJSONObject(i).getString("booking_date");
                    weight[i]=ja1.getJSONObject(i).getString("weight");
                    amount[i]=ja1.getJSONObject(i).getString("amount");
                    length[i]=ja1.getJSONObject(i).getString("length");
                    width[i]=ja1.getJSONObject(i).getString("width");
                    value[i]="Weight: "+weight[i]+"\nLength: "+length[i]+"\nWidth: "+width[i]+"\nAmount: "+amount[i]+"\nfromlocation: "+fromlocation[i]+"\ntolocation: "+tolocation[i]+"\nBookingDate: "+bookingdate[i]+"\nBookingstatus: "+bookingstatus[i];

                }
                ArrayAdapter<String> ar=new ArrayAdapter<String>(getApplicationContext(),android.R.layout.simple_list_item_1,value);
                l1.setAdapter(ar);
            }


        }

        catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
        }
    }
    public void onBackPressed()
    {
        // TODO Auto-generated method stub
        super.onBackPressed();
        Intent b=new Intent(getApplicationContext(),Userhome.class);
        startActivity(b);
    }

    @Override
    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
        oids=oid[position];
        amounts=amount[position];
        dids=did[position];
        stat=bookingstatus[position];
        if (stat.equalsIgnoreCase("confirm")) {


            final CharSequence[] items = {"Payment", "Cancel"};

            AlertDialog.Builder builder = new AlertDialog.Builder(Userviewbookedcargo.this);
            // builder.setTitle("Add Photo!");
            builder.setItems(items, new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int item) {

                    if (items[item].equals("Payment")) {

                        startActivity(new Intent(getApplicationContext(), Usermakepayment.class));
                    }

                    else if (items[item].equals("Cancel")) {
                        dialog.dismiss();
                    }
                }

            });
            builder.show();
        }
       else if (stat.equalsIgnoreCase("pickup")) {


            final CharSequence[] items = {"Track cargo", "Cancel"};

            AlertDialog.Builder builder = new AlertDialog.Builder(Userviewbookedcargo.this);
            // builder.setTitle("Add Photo!");
            builder.setItems(items, new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int item) {

                      if (items[item].equals("Track cargo")) {

                        startActivity(new Intent(getApplicationContext(), Userviewdeliveryboys.class));
                    }
                     else if (items[item].equals("Cancel")) {
                        dialog.dismiss();
                    }
                }

            });
            builder.show();
        }

    }
}