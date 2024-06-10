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
import android.widget.ListView;
import android.widget.Spinner;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class Usersendcomplaints extends AppCompatActivity implements JsonResponse, AdapterView.OnItemSelectedListener {
    EditText e1;
    String complaint;
    Button b1;
    ListView l1;
    Spinner s1;
    public static String bids;
    String[] complaints,reply,date,value,branchname,bid;
    SharedPreferences sh;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_usersendcomplaints);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        e1=(EditText)findViewById(R.id.etcomplaint);
        b1=(Button)findViewById(R.id.button);
        s1=(Spinner)findViewById(R.id.spinner);
        s1.setOnItemSelectedListener(this);
        JsonReq JR1=new JsonReq();
        JR1.json_response=(JsonResponse)Usersendcomplaints.this;
        String q1="/userviewbranch";
        q1=q1.replace(" ","%20");
        JR1.execute(q1);

        l1=(ListView)findViewById(R.id.lvview);

        JsonReq JR=new JsonReq();
        JR.json_response=(JsonResponse)Usersendcomplaints.this;
        String q="/userviewcomplaints?lid="+sh.getString("log_id","")+"&bid="+bids;
        q=q.replace(" ","%20");
        JR.execute(q);


        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                complaint=e1.getText().toString();
                if(complaint.equalsIgnoreCase("")|| !complaint.matches("[a-zA-Z ]+"))
                {
                    e1.setError("Enter your complaint");
                    e1.setFocusable(true);
                }
                else {

                    JsonReq JR = new JsonReq();
                    JR.json_response = (JsonResponse) Usersendcomplaints.this;
                    String q = "/usermanagecomplaints?complaint=" + complaint + "&lid=" + sh.getString("log_id", "") + "&bid=" + bids;
                    q = q.replace(" ", "%20");
                    JR.execute(q);
                }
            }
        });
    }

    @Override
    public void response(JSONObject jo) {

        try {

            String method=jo.getString("method");
            if(method.equalsIgnoreCase("usermanagecomplaints")) {

                String status = jo.getString("status");
                Log.d("pearl", status);


                if (status.equalsIgnoreCase("success")) {
                    Toast.makeText(getApplicationContext(), "ADDED SUCCESSFULLY", Toast.LENGTH_LONG).show();
                    startActivity(new Intent(getApplicationContext(), Usersendcomplaints.class));

                } else {

                    Toast.makeText(getApplicationContext(), " failed.TRY AGAIN!!", Toast.LENGTH_LONG).show();
                }
            }
            else if(method.equalsIgnoreCase("userviewcomplaints"))
            {
                String status=jo.getString("status");
                Log.d("pearl",status);


                if(status.equalsIgnoreCase("success")){
                    JSONArray ja1=(JSONArray)jo.getJSONArray("data");
                    branchname=new String[ja1.length()];
                    complaints=new String[ja1.length()];
                    reply=new String[ja1.length()];
                    date=new String[ja1.length()];
                    value=new String[ja1.length()];

                    for(int i = 0;i<ja1.length();i++)
                    {
                        complaints[i]=ja1.getJSONObject(i).getString("feedback_description");
                        branchname[i]=ja1.getJSONObject(i).getString("branch_name");
                        reply[i]=ja1.getJSONObject(i).getString("reply");
                        date[i]=ja1.getJSONObject(i).getString("feedback_date");
                        value[i]="Feedback: "+complaints[i]+"\nBranch Name: "+branchname[i]+"\nReply: "+reply[i]+"\nDate: "+date[i];

                    }
                    ArrayAdapter<String> ar=new ArrayAdapter<String>(getApplicationContext(),android.R.layout.simple_list_item_1,value);
                    l1.setAdapter(ar);
                }
            }
            else if(method.equalsIgnoreCase("userviewbranch"))
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

    @Override
    public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
        bids=bid[position];
    }

    @Override
    public void onNothingSelected(AdapterView<?> parent) {

    }
}