package com.example.c_bin;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RatingBar;
import android.widget.Spinner;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class customerrating extends AppCompatActivity implements JsonResponse, AdapterView.OnItemSelectedListener {
    RatingBar r1;
    Button b1;
    String rate,comment;
    public static String bids;

    EditText e1;
    Spinner s1;
    String[] branchname,bid,value;
    Float rated;
    SharedPreferences sh;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_customerrating);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        r1 = (RatingBar) findViewById(R.id.etrate);
        b1=(Button)findViewById(R.id.button);
        e1=(EditText)findViewById(R.id.etcomment);
        // l1=(ListView)findViewById(R.id.lvview);
        JsonReq JR=new JsonReq();
        JR.json_response=(JsonResponse)customerrating.this;
        String q="/customerviewrating?lid="+sh.getString("log_id","")+"&bid="+bids;
        q=q.replace(" ","%20");
        JR.execute(q);
        s1=(Spinner)findViewById(R.id.spinner);
        s1.setOnItemSelectedListener(this);
        JsonReq JR1=new JsonReq();
        JR1.json_response=(JsonResponse)customerrating.this;
        String q1="/userviewbranchss";
        q1=q1.replace(" ","%20");
        JR1.execute(q1);


        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                float rating =  r1.getRating();
                comment=e1.getText().toString();
                JsonReq JR = new JsonReq();
                JR.json_response = (JsonResponse) customerrating.this;
                String q ="/customerrating?rate="+rating+"&comment="+comment+"&lid="+sh.getString("log_id","")+"&bid="+bids;
                q = q.replace(" ", "%20");
                JR.execute(q);
            }
        });



    }

    @Override
    public void response(JSONObject jo) {
        try {

            String method = jo.getString("method");
            if (method.equalsIgnoreCase("customerrating")) {
                String status = jo.getString("status");
                Log.d("pearl", status);


                if (status.equalsIgnoreCase("success")) {
                    Toast.makeText(getApplicationContext(), "ADDED SUCCESSFULLY", Toast.LENGTH_LONG).show();
                    startActivity(new Intent(getApplicationContext(), customerrating.class));

                } else {


                    Toast.makeText(getApplicationContext(), " failed.TRY AGAIN!!", Toast.LENGTH_LONG).show();
                }
            } else if (method.equalsIgnoreCase("customerviewrating")) {
                String status = jo.getString("status");
                Log.d("pearl", status);


                if (status.equalsIgnoreCase("success")) {

                    rate=jo.getString("data");

                    rated=Float.parseFloat(rate);
                    e1.setText(jo.getString("review"));
                    Toast.makeText(getApplicationContext(),rated+"", Toast.LENGTH_SHORT).show();
                    r1.setRating(rated);

                }

            }
            else if(method.equalsIgnoreCase("userviewbranchss"))
            {
                String status=jo.getString("status");
                Log.d("pearl",status);


                if(status.equalsIgnoreCase("success")){
                    JSONArray ja1=(JSONArray)jo.getJSONArray("data");
                    branchname=new String[ja1.length()];

                    bid=new String[ja1.length()];
                    value=new String[ja1.length()];

                    for(int i = 0;i<ja1.length();i++)
                    {

                        branchname[i]=ja1.getJSONObject(i).getString("branch_name");
                        bid[i]=ja1.getJSONObject(i).getString("branch_id");

                        value[i]="Branch Name: "+branchname[i];

                    }
                    ArrayAdapter<String> ar=new ArrayAdapter<String>(getApplicationContext(),android.R.layout.simple_list_item_1,value);
                    s1.setAdapter(ar);
                }
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
    public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
        bids=bid[position];
    }

    @Override
    public void onNothingSelected(AdapterView<?> parent) {

    }
}